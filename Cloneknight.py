import pygame
pygame.init()

#ขนาดจอ
w_height = 600
w_width = 1000

title = pygame.display.set_caption('Cloneknight')
screen = pygame.display.set_mode((w_width, w_height))

run = True
#ตัวเกม-------------------------------------------------------------------------------------------------------------------------------------
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill('gray')
    pygame.display.update()
pygame.QUIT


    