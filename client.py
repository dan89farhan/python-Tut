import socket
import threading

"""This is used to import socket library"""


class Client(threading.Thread):

    """This is client class to use for client """

    def __init__(self):
        """Initialization of method"""
        threading.Thread.__init__(self)
        self.port = 9090
        self.socket_details = socket.socket()
        self.hostname = socket.gethostname()
        self.circuit = ''

    def connect_to_server(self):
        """This method is use connect to server"""
        print("The value of socket address is ", self.hostname)
        self.socket_details.connect((self.hostname, self.port))

    def receive_message(self):
        """Receive Message from server endlessly"""
        while True:
            message = self.socket_details.recv(1024)
            print(message)
            if message == "exit":
                return    
        

    def run(self):
        """Backgound RUN METHOD"""
        print("Enter 'exit' to stop the client")
        while True:
            print("Now you can send message to the server ")
            print("Enter your message")
            message = input()
            if message == "exit":
                return 0
            else:

                message = bytes(message, 'utf-8')
                print(message)
                encrypt = ''
                for chars in enumerate(message):

                    encrypt += chr(chars[1] - 3)
                    
                
                encrypt = "[sent from client] > " + encrypt
                print(encrypt)
                self.socket_details.send(encrypt.encode())


C = Client()
C.connect_to_server()
C.start()
C.receive_message()

C.join()
print("Client has been shut down")
