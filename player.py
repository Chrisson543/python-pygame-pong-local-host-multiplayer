import pygame


class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.velocity = 5
        self.color = color

    def movement(self):
        keys = pygame.key.get_pressed()

        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

        if keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_s]:
            self.rect.y += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, screen):
        self.movement()
        self.draw(screen)
