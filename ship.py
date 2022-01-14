import pygame

class Ship():
    '''initialize the ship'''
    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()#treat image as rectangle
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #set decimal value for ship center
        self.center = float(self.rect.centerx)
        # movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        '''update the ship position depend on movement_flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        #update ship location
        self.rect.centerx = self.center

    def builtme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image,self.rect)
    '''
    def left_right_jump(self):
        self.loc_x = self.screen_rect.left
        self.div = self.screen_rect.right - self.screen_rect.left
        self.init = self.screen_rect.left + self.rect.right
        while True:
            self.rect.right = self.init % (self.div)
            pygame.time.wait(2)
            self.init = self.init + 1
            self.builtme()
            pygame.display.flip()
    '''