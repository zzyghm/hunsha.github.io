import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

PORT = 8000
Handler = MyHttpRequestHandler

with socketserver.TCPServer(("192.168.168.3", PORT), Handler) as httpd:
    print(f"Server started at http://192.168.168.3:{PORT}")
    httpd.serve_forever()
