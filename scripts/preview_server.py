#!/usr/bin/env python3
"""
Infographic Interactive Builder — Local Preview Server

Watches .infographic/.preview.html and serves it in the browser with auto-reload.
No external dependencies — stdlib only.

Usage:
    python scripts/preview_server.py
    python scripts/preview_server.py --port 7783
    python scripts/preview_server.py --file .infographic/.preview.html
"""

import argparse
import http.server
import json
import os
import socketserver
from pathlib import Path

PORT = 7783
DEFAULT_PREVIEW_FILE = Path(".infographic/.preview.html")

# Injected into every served page — polls /mtime every 600ms and reloads on change
RELOAD_SCRIPT = """
<script>
(function() {
  var lastMtime = null;
  function check() {
    fetch('/__mtime__')
      .then(function(r) { return r.json(); })
      .then(function(data) {
        if (lastMtime === null) { lastMtime = data.mtime; return; }
        if (data.mtime !== lastMtime) { window.location.reload(); }
      })
      .catch(function() {});
  }
  setInterval(check, 600);
})();
</script>
"""

WAITING_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Infographic Preview</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0D0D0D;
      color: #8B8B8B;
      font-family: 'Inter', sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      gap: 20px;
    }
    .dots {
      display: flex;
      gap: 8px;
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #E99A00;
      animation: pulse 1.4s ease-in-out infinite;
    }
    .dot:nth-child(2) { animation-delay: 0.2s; }
    .dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes pulse {
      0%, 100% { opacity: 0.15; transform: scale(0.8); }
      50%       { opacity: 1;    transform: scale(1); }
    }
    p {
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #555;
    }
  </style>
</head>
<body>
  <div class="dots">
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
  </div>
  <p>Waiting for component...</p>
</body>
</html>
"""


class PreviewHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/__mtime__":
            self._serve_mtime()
        elif self.path in ("/", "/index.html"):
            self._serve_preview()
        else:
            self.send_error(404)

    def _serve_mtime(self):
        try:
            mtime = preview_file.stat().st_mtime
        except FileNotFoundError:
            mtime = 0

        body = json.dumps({"mtime": mtime}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def _serve_preview(self):
        try:
            content = preview_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            content = WAITING_PAGE

        # Inject reload script
        if "</body>" in content:
            content = content.replace("</body>", RELOAD_SCRIPT + "\n</body>", 1)
        else:
            content += RELOAD_SCRIPT

        body = content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # suppress per-request logs


def main():
    global preview_file

    parser = argparse.ArgumentParser(description="Infographic preview server with auto-reload")
    parser.add_argument("--port", type=int, default=PORT, help=f"Port to serve on (default: {PORT})")
    parser.add_argument("--file", type=str, default=str(DEFAULT_PREVIEW_FILE), help="Preview HTML file to watch")
    args = parser.parse_args()

    preview_file = Path(args.file)
    preview_file.parent.mkdir(parents=True, exist_ok=True)

    with socketserver.TCPServer(("localhost", args.port), PreviewHandler) as server:
        server.allow_reuse_address = True
        url = f"http://localhost:{args.port}"
        print(f"  Preview server → {url}")
        print(f"  Watching       → {preview_file.resolve()}")
        print(f"  Auto-reloads on every component render. Ctrl+C to stop.\n")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n  Preview server stopped.")


if __name__ == "__main__":
    main()
