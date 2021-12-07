import sys

import http.server
import socketserver

DEFAULT_PORT = 8000


class QuickServer(socketserver.TCPServer):
    def __init__(self, port: int = DEFAULT_PORT) -> None:
        self.port = port
        self.allow_reuse_address = True

        handler = http.server.SimpleHTTPRequestHandler
        server_address = ("localhost", self.port)
        super().__init__(server_address, handler)

    def run(self, poll_interval: float = 0.5) -> None:
        super().serve_forever(poll_interval=poll_interval)

    def stop(self) -> None:
        super().shutdown()


def main():
    try:
        port = int(sys.argv[1])
    except:
        port = DEFAULT_PORT

    try:
        print(f"\n\nServing at port {port}. Press Ctrl+C to stop.")
        print(f"http://localhost:{port}/\n")
        server = QuickServer(port=port)
        server.run()
    except KeyboardInterrupt:
        print(f"\nShutting down server at port {port}...")
        server.stop()


if __name__ == "__main__":
    main()
