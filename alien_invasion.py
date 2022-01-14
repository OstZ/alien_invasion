import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    #ship
    ship = Ship(screen,ai_settings)
    #bullets
    bullets = Group()


    bg_color = (230,230,230)
    while True:
        gf.check_events(ai_settings,ship,screen,bullets)
        ship.update()
        bullets.update()
        #deal with old bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()