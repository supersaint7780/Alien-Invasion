import pygame, os

class Alien():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.WIDTH = 55
        self.HEIGHT = 40
        self.VELOCITY = 2
        self.IMAGE_PATH = os.path.join('Assests', 'spaceship_yellow.png')
        self.IMAGE = pygame.transform.scale(
            pygame.image.load(self.IMAGE_PATH), (self.WIDTH, self.HEIGHT))
        self.rect = self.IMAGE.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def blitme(self):
        self.screen.blit(self.IMAGE, self.rect)

    def update(self, direction):
        self.rect.x += self.VELOCITY * direction
    
    def drop(self):
        self.rect.y += self.settings.ALIEN_DROP_VELOCITY
    
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False