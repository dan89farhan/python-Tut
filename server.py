import socket
import threading


class ServerSocket(threading.Thread):
    """The main server which runs in background."""

    def __init__(self):
        threading.Thread.__init__(self)
        self.port = 9090
        self.socket_details = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.circuit = ""
        self.add = ""

    def create_connection(self):
        """For create connection"""
        self.socket_details.bind((self.hostname, self.port))
        # self.socket_details.connect((self.hostname, self.port))
        self.socket_details.listen(5)
        
        print(self.socket_details)

    def receive_message(self):
        """Receive Message from server endlessly"""
        while True:
            try:
                if self.add != "":
                    message = self.circuit.recv(1024)
                    print("[recieved from client] > "+ message)
                    if message == "exit":
                        return
            except ValueError:
                print("Got an error ", ValueError)    

    def run(self):
        """Backgound RUN METHOD"""
        self.circuit, self.add = self.socket_details.accept()
        print("Receive new connection from clint ", self.add)
        print("Enter 'exit' to stop the server")
        while True:
            
            print("Enter your message")
            message = input()
            if message == "exit":
            
                return
            else:

                message = bytes(message, 'utf-8')
                print(message)
                encrypt = ''
                for chars in enumerate(message):
                    
                    encrypt += chr(chars[1] + 3)
                    # print(bytes([chars[1] + 3]))
                encrypt = "[sent from server] > " + encrypt
                print(encrypt)
                self.circuit.send(encrypt.encode())


S = ServerSocket()

S.create_connection()
S.start()
S.receive_message()
S.join()
print("Server has beed shut down.")
S.circuit.close()
