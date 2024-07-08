import pygame
pygame.init()


w_height = 1000
w_width = 600
title = pygame.display.set_caption('Cloneknight')
screen = pygame.display.set_mode((w_height,w_width))

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill('gray')
    pygame.display.update()
pygame.QUIT


    