import pygame

class Bullet():
    def __init__(self, screen, ship):
        self.screen = screen
        self.VELOCITY = 7
        self.WIDTH = 5
        self.HEIGHT = 10
        self.COLOR = (255, 0, 0) #red
        self.rect = pygame.Rect(
            ship.rect.x + ship.rect.width/2, ship.rect.y, self.WIDTH, self.HEIGHT)
    
    def blitme(self):
        pygame.draw.rect(self.screen, self.COLOR ,self.rect)

    def update(self):
        self.rect.y -= self.VELOCITY
