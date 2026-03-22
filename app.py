from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello DevOps super deployment Manivasagam!".encode())

port = int(os.environ.get("PORT", 8080))

server = HTTPServer(('0.0.0.0', port), handler)
print(f"Server running on port {port}...")
server.serve_forever()
