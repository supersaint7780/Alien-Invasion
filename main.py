import pygame, sys
from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet

def draw_window(background, screen, ship, aliens_matrix, bullet_list):
    screen.blit(background, (0, 0))
    ship.blitme()
    for alien_row in aliens_matrix:
        for alien in alien_row:
            alien.blitme()
    for bullet in bullet_list:
        bullet.blitme()
    pygame.display.update()

def drop_alien_fleet(aliens):
    for alien_row in aliens:
        for alien in alien_row:
            alien.drop()

def create_alien_fleet(settings, screen, aliens_matrix):
    #create a full fleet of aliens
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    #determining the number of aliens in a row
    available_space_x = settings.SCREEN_WIDTH - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #determining the number of rows of aliens
    available_space_y = settings.SCREEN_HEIGHT - 6 * alien_height
    number_rows = int(available_space_y / (2 * alien_height))

    for row_number in range(number_rows):
        alien_row = []
        for alien_number in range(number_aliens_x):
            alien = Alien(screen)
            alien.rect.x = alien_width + 2 * alien_number * alien_width
            alien.rect.y = alien_height + 2 * row_number * alien_height
            alien_row.append(alien)
        aliens_matrix.append(alien_row)
        
def change_fleet_direction(aliens_matrix, direction):
    for alien_row in aliens_matrix:
        changed = False
        for alien in alien_row:
            if alien.check_edge():
                direction *= -1
                drop_alien_fleet(aliens_matrix)
                changed = True
                break
        if changed:
            break
    return direction

def handle_collision(bullet_list, aliens_matrix):
    for bullet in bullet_list:
        for alien_row in aliens_matrix:
            for alien in alien_row:
                if alien.rect.colliderect(bullet):
                    alien_row.remove(alien)
                    bullet_list.remove(bullet)

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
    aliens_matrix = []
    create_alien_fleet(game_settings, SCREEN, aliens_matrix)
    fleet_direction = 1
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
                    bullet = Bullet(SCREEN, ship)
                    bullet_list.append(bullet)
                
                #keyboard shortcut to quit the game
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        #invoking the method to handle the movement of ship
        ship.handle_movement()
        
        #handling the movement of bullets
        for bullet in bullet_list:
            bullet.update()
            if bullet.rect.y < 0:
                bullet_list.remove(bullet)
        
        #handling alien-bullet collision
        handle_collision(bullet_list, aliens_matrix)

        fleet_direction = change_fleet_direction(aliens_matrix, fleet_direction)
        for alien_row in aliens_matrix:
            for alien in alien_row:
                alien.update(fleet_direction)
        
        #ending the game if alien collides with ship
        for alien_row in aliens_matrix:
            for alien in alien_row:
                if alien.rect.colliderect(ship) or alien.rect.bottom >= game_settings.SCREEN_HEIGHT:
                    pygame.time.delay(2000)
                    pygame.quit()
                    sys.exit()
                
        #drawing items to the screen
        draw_window(BACKGROUND, SCREEN, ship, aliens_matrix, bullet_list)


#running the game
main()