import pygame 

pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 600
screen_surf = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
title = pygame.display.set_caption("clone knight")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen_surf.fill((240, 240, 240))
    pygame.display.update()

pygame.quit()