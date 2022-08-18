import pygame, sys
from settings import Settings
from ship import Ship


def main():

    # initializing pygame, settings, clock, ship and screen objects
    pygame.init()
    game_settings = Settings() 
    ship_properties = Ship()
    SCREEN = pygame.display.set_mode(
        (game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()

    #loading the background image after resizing to appropriate size
    BACKGROUND = pygame.transform.scale(
        pygame.image.load(game_settings.BACKGROUND_IMAGE_PATH),
        (game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
    
    #loading the ship image after resizing to appropriate size
    SHIP = pygame.transform.rotate(
        pygame.transform.scale(
        pygame.image.load(ship_properties.SHIP_IMAGE_PATH),
        (ship_properties.SHIP_WIDTH, ship_properties.SHIP_HEIGHT)), 180)

    #creating a rectangle within which the ship will be drawn
    ship_rect = pygame.Rect(game_settings.SCREEN_WIDTH//2 - ship_properties.SHIP_WIDTH//2,
            game_settings.SCREEN_HEIGHT - ship_properties.SHIP_HEIGHT - 10,
            ship_properties.SHIP_WIDTH,
            ship_properties.SHIP_HEIGHT)

    #list of bullets on screen
    bullets = []

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
                if event.key == pygame.K_SPACE and len(bullets) < ship_properties.MAX_BULLETS:
                    bullet = pygame.Rect(
                        ship_rect.x + ship_rect.width/2, ship_rect.y , 5, 10)
                    bullets.append(bullet)
        
        #handling the movement of ships
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and ship_rect.x > 0:
            ship_rect.x -= ship_properties.SHIP_VELOCITY
        if keys_pressed[pygame.K_RIGHT] and ship_rect.x < game_settings.SCREEN_WIDTH - ship_properties.SHIP_WIDTH:
            ship_rect.x += ship_properties.SHIP_VELOCITY
        
        #handling the movement of bullets
        for bullet in bullets:
            bullet.y -= ship_properties.BULLET_VELOCITY
            if bullet.y < 0:
                bullets.remove(bullet)

        #drawing items to the screen
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(SHIP, (ship_rect.x, ship_rect.y))
        for bullet in bullets:
            pygame.draw.rect(SCREEN, game_settings.color['RED'], bullet)
        pygame.display.update()


#running the game
main()