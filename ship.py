import os, pygame


class Ship():

    #initialize the ship properties its starting position
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.WIDTH = 55
        self.HEIGHT = 40
        self.VELOCITY = 5
        self.IMAGE_PATH = os.path.join('Assests', 'spaceship_red.png')
        self.IMAGE = pygame.transform.rotate(
            pygame.transform.scale(
            pygame.image.load(self.IMAGE_PATH),
            (self.WIDTH, self.HEIGHT)), 180)
        self.rect = self.IMAGE.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.MAX_BULLETS = 4
    
    #method to draw the ship to the screen
    def blitme(self):
        self.screen.blit(self.IMAGE, self.rect)

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.VELOCITY
        if keys_pressed[pygame.K_RIGHT] and self.rect.x < self.screen_rect.width - self.WIDTH:
            self.rect.x += self.VELOCITY