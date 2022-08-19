import pygame, sys
from settings import Settings
from ship import Ship
from bullet import Bullet


def main():

    # initializing pygame, settings, clock, ship and screen objects
    pygame.init()
    game_settings = Settings() 
    SCREEN = pygame.display.set_mode(
        (game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    ship = Ship(SCREEN)
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()

    #loading the background image after resizing to appropriate size
    BACKGROUND = pygame.transform.scale(
        pygame.image.load(game_settings.BACKGROUND_IMAGE_PATH),
        (game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))

    #list of bullets on screen
    bullet_list = []

    #Starting the main game loop
    while True:

        #limiting the loop to max 60 times per second
        clock.tick(game_settings.FPS)

        #looking for event(keyboard and mouse clicks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #firing bullets by pressing spacebar
                if event.key == pygame.K_SPACE and len(bullet_list) < ship.MAX_BULLETS:
                    bullet = Bullet(SCREEN, ship, game_settings)
                    bullet_list.append(bullet)
        
        #ivoking the method to handle the movement of ship
        ship.handle_movement()
        
        #handling the movement of bullets
        for bullet in bullet_list:
            bullet.rect.y -= bullet.VELOCITY
            if bullet.rect.y < 0:
                bullet_list.remove(bullet)

        #drawing items to the screen
        SCREEN.blit(BACKGROUND, (0, 0))
        ship.blitme()
        for bullet in bullet_list:
            bullet.blitme()
        pygame.display.update()


#running the game
main()