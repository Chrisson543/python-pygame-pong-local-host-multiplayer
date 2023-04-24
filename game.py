import pygame
from player import Player
from client import Client

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

print('1')
client = Client()
print('2')
player = client.get_player()
print('3')

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    data = client.get_data(player)

    opponent = data[0]
    ball = data[1]
    player.update(screen)
    opponent.draw(screen)
    ball.draw(screen)
    pygame.display.update()
    clock.tick(60)