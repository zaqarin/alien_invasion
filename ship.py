import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.centerx < self.screen_rect.right-self.rect.width/2 - 5:
            self.rect.centerx += self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.centerx > self.screen_rect.left + self.rect.width/2 + 5:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

        # elif self.moving_up:
        #     if self.rect.top == self.screen_rect.top:
        #         pass
        #     else:
        #         self.rect.bottom -= self.ai_settings.ship_speed_factor
        #
        # elif self.moving_down:
        #     if self.rect.bottom == self.screen_rect.bottom:
        #         pass
        #     else:
        #         self.rect.bottom += self.ai_settings.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)