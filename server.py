import socketserver
import requests


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Do functions
        if self.data == b'weather':
            response = requests.request("GET", "https://community-open-weather-map.p.rapidapi.com/weather", headers={'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",'x-rapidapi-key': "3a1ec944ea093518de7458f211bd365d"
    }, params= {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"budapest%2Chu"}g)
            self.request.sendall(b'excuse me wtf')
            print(response.text)
            return
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "192.168.0.33", 80

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
