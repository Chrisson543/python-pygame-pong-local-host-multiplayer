import socket
import pickle


class Client:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5050
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def get_player(self):
        return pickle.loads(self.client.recv(1024))

    def get_data(self, player):
        self.client.send(pickle.dumps(player))
        return pickle.loads(self.client.recv(1024))
