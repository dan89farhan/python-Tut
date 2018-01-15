import socket

"""This is used to import socket library"""

class Client:

    """This is client class to use for client """

    def __init__(self):

        self.port = 9090
        self.socket_details = socket.socket()
        self.hostname = socket.gethostname()

    def connect_to_server(self):
        """This method is use connect to server"""
        print("The value of socket address is ", self.hostname)
        self.socket_details.connect((self.hostname, self.port))
        print(self.socket_details.recv(1024))
        self.socket_details.close()
C = Client()
C.connect_to_server()
