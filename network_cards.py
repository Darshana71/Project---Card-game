import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.106"
        self.port = 1234
        self.addr = (self.server, self.port)
        self.num = self.connect()

    def getNum(self):
        return self.num

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def recv(self, msg):
        return self.client.recv(2048).decode("utf-8")


