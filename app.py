from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello DevOps Manivasagam vaazhthukkal!")

server = HTTPServer(('0.0.0.0', 3000), handler)
print("Server running on port 3000...")
server.serve_forever()
