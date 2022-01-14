import sys
import pygame
from bullets import Bullet

def check_events(ai_settings,ship,screen,bullets):
    '''respond to keypress and mouse events'''

    def check_keydown_events(event,ship,ai_settings,bullets,screen):
        '''check keypress'''
        if event.key == pygame.K_d:
            ship.moving_right = True
        elif event.key == pygame.K_a:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

    def check_keyup_events(event,ship):
        '''check keyup'''
        if event.key == pygame.K_d:
            ship.moving_right = False
        elif event.key == pygame.K_a:
            ship.moving_left = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_settings,bullets,screen)
        #move the ship to the right
        #ship.rect.centerx += 1
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def update_screen(ai_settings,screen,ship,bullets):
    '''Update images on the screen and flip to the new screen.'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.builtme()

    pygame.display.flip()

