import pygame

class Bullet():
    def __init__(self, screen, ship, settings):
        self.screen = screen
        self.settings = settings
        self.VELOCITY = 7
        self.WIDTH = 5
        self.HEIGHT = 10
        self.rect = pygame.Rect(
            ship.rect.x + ship.rect.width/2, ship.rect.y, self.WIDTH, self.HEIGHT)
    
    def blitme(self):
        pygame.draw.rect(self.screen, self.settings.color['RED'] ,self.rect)
