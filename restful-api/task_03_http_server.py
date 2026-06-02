#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""

import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Routing class"""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}

            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Comtent-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "desciription": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """8000 port run"""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port {}".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\Stopping server...")
        httpd.server_close()


if __name__ == "__main__":
    run()
