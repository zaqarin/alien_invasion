import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai = Settings()
    screen = pygame.display.set_mode((ai.width, ai.height))
    sh = Ship(ai, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai, screen, sh, aliens)
    pygame.display.set_caption('Alien Invasion')

    while True:
        gf.check_events(ai, screen, sh, bullets)
        sh.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai, aliens)
        gf.update_screen(ai, screen, sh, aliens, bullets)

run_game()