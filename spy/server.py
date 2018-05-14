from http.server import SimpleHTTPRequestHandler, socketserver

class SpyRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        print(body)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

server = socketserver.TCPServer(('', 8080), SpyRequestHandler)
server.serve_forever()