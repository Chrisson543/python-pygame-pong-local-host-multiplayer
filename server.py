import pickle
import socket
import threading
from player import Player
from ball import Ball
import pygame

host = 'localhost'
port = 5050
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

players = {
    'player_1': {
        'player': Player(50, 250, (55, 155, 255))
    },
    'player_2': {
        'player': Player(550, 250, (255, 155, 55))
    }
}
ball = Ball(295, 295, (155, 155, 155))
clock = pygame.time.Clock()

clients = []

server.listen()
print('Server started. Waiting for connections...')

current_player_id = 1
ball_running = False

def handle_ball():
    while True:
        ball.update([players['player_1']['player'], players['player_2']['player']])
        clock.tick(60)


def handle_client(client, id):
    global current_player_id
    client.send(pickle.dumps(players[f'player_{id}']['player']))

    while True:
        try:
            player = pickle.loads(client.recv(1024))
            players[f'player_{id}']['player'] = player

            if id == 1:
                client.send(pickle.dumps([players['player_2']['player'], ball]))
            else:
                client.send(pickle.dumps([players['player_1']['player'], ball]))
        except:
            print(f'player_{id} disconnected')
            clients.remove(client)
            if id == 1:
                current_player_id = 1
            elif id == 2:
                current_player_id = 2
            break


while True:
    client, address = server.accept()
    clients.append(client)
    print(f'player {current_player_id} connected from {address}')

    threading.Thread(target=handle_client, args=(client, current_player_id)).start()
    if current_player_id == 2 and not ball_running:
        threading.Thread(target=handle_ball).start()
        ball_running = True

    current_player_id += 1



