#!/usr/bin/env python3
"""
Infographic Export Script
Converts HTML infographics to PNG (retina) and PDF using Playwright.

Usage:
    python export.py --input infographic.html --output infographic.png --format png
    python export.py --input infographic.html --output infographic.pdf --format pdf
    python export.py --input infographic.html --output infographic --format all

    # Recommended: use --serve so Google Fonts + Phosphor Icons CDN load correctly
    python export.py --input infographic.html --output infographic --format all --serve

Install dependencies:
    pip install playwright --break-system-packages -q
    playwright install chromium --with-deps
"""

import argparse
import os
import sys
import threading
import http.server
import socketserver
from pathlib import Path


def check_dependencies():
    """Verify Playwright is installed and Chromium is available."""
    try:
        from playwright.sync_api import sync_playwright
        return True
    except ImportError:
        print("ERROR: Playwright not installed.")
        print("Run: pip install playwright --break-system-packages -q")
        print("Then: playwright install chromium --with-deps")
        return False


def start_local_server(directory: str, port: int = 8765):
    """
    Spin up a temporary HTTP server so that file:// CDN requests
    (Google Fonts, Phosphor Icons) resolve correctly in Playwright.
    Returns (server, url_base).
    """
    handler = http.server.SimpleHTTPRequestHandler
    handler.log_message = lambda *args: None  # silence request logs

    os.chdir(directory)
    server = socketserver.TCPServer(("", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, f"http://localhost:{port}"


def wait_for_render(page, extra_ms: int = 300):
    """
    Wait until network is idle (CDN fonts + icon scripts loaded),
    then allow a small buffer for CSS animations to reach their end state.
    """
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        pass  # networkidle timeout is non-fatal — carry on
    page.wait_for_timeout(extra_ms)


def export_png(html_path: str, output_path: str, width: int = 1100, scale: int = 2, serve: bool = True):
    """Export HTML infographic to retina PNG."""
    from playwright.sync_api import sync_playwright

    abs_html = os.path.abspath(html_path)
    if not os.path.exists(abs_html):
        print(f"ERROR: HTML file not found: {abs_html}")
        sys.exit(1)

    html_dir = str(Path(abs_html).parent)
    html_filename = Path(abs_html).name

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": width, "height": 800},
            device_scale_factor=scale
        )

        if serve:
            # We must serve from the current working directory (repo root) 
            # so that relative assets (if any) or subfolders resolve correctly
            server, base_url = start_local_server(os.getcwd())
            # Convert absolute path to a path relative to the repo root
            try:
                rel_path = os.path.relpath(abs_html, os.getcwd())
                # Replace Windows backslashes with forward slashes for the URL
                url_path = rel_path.replace('\\', '/')
                url = f"{base_url}/{url_path}"
            except ValueError:
                # If path isn't relative to cwd, fallback to serving the specific folder
                server, base_url = start_local_server(html_dir)
                url = f"{base_url}/{html_filename}"
        else:
            url = f"file://{abs_html}"

        page.goto(url)
        wait_for_render(page)

        # Measure actual content height and resize viewport to match
        height = page.evaluate("document.documentElement.scrollHeight")
        page.set_viewport_size({"width": width, "height": height})
        wait_for_render(page, extra_ms=200)

        page.screenshot(path=output_path, full_page=True)
        browser.close()

        if serve:
            server.shutdown()

    print(f"PNG exported: {output_path} ({width * scale}x{height * scale} px)")


def export_pdf(html_path: str, output_path: str, width: int = 1100, serve: bool = True):
    """Export HTML infographic to PDF."""
    from playwright.sync_api import sync_playwright

    abs_html = os.path.abspath(html_path)
    if not os.path.exists(abs_html):
        print(f"ERROR: HTML file not found: {abs_html}")
        sys.exit(1)

    html_dir = str(Path(abs_html).parent)
    html_filename = Path(abs_html).name

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": 800})

        if serve:
            server, base_url = start_local_server(html_dir, port=8766)
            url = f"{base_url}/{html_filename}"
        else:
            url = f"file://{abs_html}"

        page.goto(url)
        wait_for_render(page)

        content_height = page.evaluate("document.documentElement.scrollHeight")

        page.pdf(
            path=output_path,
            print_background=True,
            width=f"{width}px",
            height=f"{content_height}px"
        )
        browser.close()

        if serve:
            server.shutdown()

    print(f"PDF exported: {output_path}")


def export_svg(pdf_path: str, output_path: str) -> bool:
    """
    Convert PDF to SVG for Figma / Illustrator / Affinity import.

    Tries Inkscape first (better output), falls back to pdf2svg.
    Returns True if successful, False if neither tool is available.
    """
    import shutil
    import subprocess

    if shutil.which("inkscape"):
        result = subprocess.run(
            ["inkscape", "--export-type=svg", pdf_path, "-o", output_path],
            capture_output=True
        )
        if result.returncode == 0:
            print(f"SVG exported: {output_path}  (via Inkscape — shapes + text as paths)")
            return True

    if shutil.which("pdf2svg"):
        result = subprocess.run(
            ["pdf2svg", pdf_path, output_path],
            capture_output=True
        )
        if result.returncode == 0:
            print(f"SVG exported: {output_path}  (via pdf2svg — shapes + text as paths)")
            return True

    print("SVG export skipped — neither Inkscape nor pdf2svg found.")
    print("  Figma alternative: drag the .pdf directly into Figma (File → Place Image, or just drop it).")
    print("  Install Inkscape:  https://inkscape.org/release/  or  brew install inkscape")
    print("  Install pdf2svg:   brew install pdf2svg  /  apt install pdf2svg")
    return False


def main():
    parser = argparse.ArgumentParser(description="Export HTML infographic to PNG/PDF/SVG")
    parser.add_argument("--input",  "-i", required=True,  help="Path to HTML infographic file")
    parser.add_argument("--output", "-o", required=True,  help="Output path (no extension needed for format=all)")
    parser.add_argument("--format", "-f", default="all",  choices=["png", "pdf", "svg", "all"], help="Export format (default: all)")
    parser.add_argument("--width",  "-w", type=int, default=1100, help="Canvas width px (default: 1100)")
    parser.add_argument("--scale",  "-s", type=int, default=2,    help="DPI scale for PNG (default: 2 = retina)")
    parser.add_argument("--serve",        action="store_true", default=True,
                        help="Serve via local HTTP so CDN fonts/icons load (default: on)")
    parser.add_argument("--no-serve",     dest="serve", action="store_false",
                        help="Disable local HTTP server (use file:// — CDN assets may not load)")

    args = parser.parse_args()

    if not check_dependencies():
        sys.exit(1)

    output_base = Path(args.output).with_suffix("")

    if args.format in ("png", "all"):
        png_path = str(output_base) + ".png"
        export_png(args.input, png_path, args.width, args.scale, serve=args.serve)

    if args.format in ("pdf", "svg", "all"):
        pdf_path = str(output_base) + ".pdf"
        export_pdf(args.input, pdf_path, args.width, serve=args.serve)

    if args.format in ("svg", "all"):
        svg_path = str(output_base) + ".svg"
        export_svg(pdf_path, svg_path)

    if args.format == "all":
        print(f"\nAll formats exported:")
        print(f"  HTML: {args.input}")
        print(f"  PNG:  {str(output_base)}.png")
        print(f"  PDF:  {str(output_base)}.pdf")
        print(f"  SVG:  {str(output_base)}.svg  ← open in Figma / Illustrator / Affinity")


if __name__ == "__main__":
    main()
