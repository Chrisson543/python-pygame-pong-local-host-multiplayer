import pygame
from time import sleep


class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.velocity = pygame.Vector2(3, 3)
        self.color = color

    def movement(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.top <= 0:
            self.velocity.y *= -1
        if self.rect.bottom >= 600:
            self.velocity.y *= -1

    def collisions(self, players):
        for player in players:
            if self.rect.colliderect(player.rect):
                self.velocity.x *= -1

        if self.rect.left <= 0:
            self.rect.x = 295
            self.rect.y = 295
            self.velocity.x *= -1
            sleep(2)
        if self.rect.right >= 600:
            self.rect.x = 295
            self.rect.y = 295
            self.velocity.x *= -1
            sleep(2)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, players):
        self.collisions(players)
        self.movement()
