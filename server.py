import socket


class ServerSocket:
    """The main server which runs in background."""

    def __init__(self):

        self.port = 9090
        self.socket_details = socket.socket()

        self.hostname = socket.gethostname()
        

    def create_connection(self):

        """For create connection"""
        self.socket_details.bind((self.hostname, self.port))
        self.socket_details.listen(5)
        print(self.socket_details)

    def send_message(self):
        """for send message"""

        circuit, add = self.socket_details.accept()
        print("Receive new connection from clint ", add)
        print("Enter your message")
        message = input()
        message = bytes(message, 'utf-8')
        encrypt = ''
        for i, chars in enumerate(message):
            
            encrypt += chr(chars+3)
            print(bytes([chars+3]))
        circuit.send(encrypt.encode())
        circuit.close()


S = ServerSocket()
S.create_connection()
S.send_message()
