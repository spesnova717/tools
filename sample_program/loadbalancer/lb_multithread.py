from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
import requests

class LoadBalancer:
    def __init__(self, host, port, backend_servers):
        self.host = host
        self.port = port
        self.backend_servers = backend_servers
        self.server_index = 0

    def start(self):
        handler = self.create_request_handler()
        server = ThreadingHTTPServer((self.host, self.port), handler)
        print(f"Starting load balancer on {self.host}:{self.port}")
        server.serve_forever()

    def create_request_handler(self):
        load_balancer = self

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                server = load_balancer.get_next_backend_server()
                try:
                    response = requests.get(f"http://{server}", timeout=5)
                    self.send_response(response.status_code)
                    self.end_headers()
                    self.wfile.write(response.content)
                except requests.RequestException as e:
                    self.send_error(500, str(e))

        return RequestHandler

    def get_next_backend_server(self):
        server = self.backend_servers[self.server_index]
        self.server_index = (self.server_index + 1) % len(self.backend_servers)
        return server

def main():
    host = 'localhost'
    port = 8000
    backend_servers = ["192.168.100.9:8888", "192.168.100.9:8888"]
    load_balancer = LoadBalancer(host, port, backend_servers)
    threading.Thread(target=load_balancer.start).start()

if __name__ == "__main__":
    main()

