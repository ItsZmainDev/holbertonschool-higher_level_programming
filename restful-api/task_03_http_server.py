#!/usr/bin/python3
"Module for make requests to a RESTful api"

import http.server
import json


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Welcome to the root endpoint!")
        elif self.path == "/data":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Here is your data.")
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Status: OK")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Error: Endpoint not found.")


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
