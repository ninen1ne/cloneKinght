import pygame 
from os.path import join
from random import randint, uniform

from settings import Settings




pygame.init()


clock = pygame.time.Clock()

settings = Settings() 
screen_surf = pygame.display.set_mode((settings.screen_height, settings.screen_width))
title = pygame.display.set_caption("clone knight")

player_rect = pygame.FRect((100, 100), (100, 200))

running = True
while running:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen_surf.fill(settings.screen_color)
    pygame.draw.rect(screen_surf, 'red', player_rect)
    pygame.display.update()

pygame.quit()