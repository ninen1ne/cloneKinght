#Run This File

import pygame
import button

pygame.init()
pygame.display.set_caption("cloneKnight")

SCREEN_H = 480
SCREEN_W = 720
screen = pygame.display.set_mode((SCREEN_W , SCREEN_H))

#background
bg = pygame.image.load("mainmenu + pausemenu/menuscreen_background.jpg")
bg = pygame.transform.scale(bg,(SCREEN_W,SCREEN_H))


#line 18-26 นำรูปและกำหนดให้เป็น button
start_img = pygame.image.load("mainmenu + pausemenu/button_start.png").convert_alpha()
start_button = button.Button(360, 140, start_img, 1)

options_img = pygame.image.load("mainmenu + pausemenu/button_options.png").convert_alpha()
options_button = button.Button(360,240, options_img, 1)

exit_img = pygame.image.load("mainmenu + pausemenu/button_exit.png").convert_alpha()
exit_button = button.Button(360,340, exit_img, 1)

WHITE = (255,255,255)
font = pygame.font.SysFont("komikaaxis", 40)


#ฟังก์ชันสร้าง text เฉยๆ
def gen_text(text, font, color, x, y):
    img = font.render(text, True , color)
    img_rect = img.get_rect(center=(x,y))
    screen.blit(img, (img_rect))


#จะเห็นว่ามี def อยู่ 3 อัน mainmenu play options
#แต่ละ def จะมีการ run screen ของตัวเอง
#เราจะให้ mainmenu เป็นตัวเริ่มแรกใ เลยสั่งใช้งานฟังก์ชัน mainmenu() ในบรรทัดล่างสุด
#จากนั้นก็ใส่ปุ่มลงไปใน mainmenu พอกดปุ่มปัปก็จะให้มันไปทำงานอีกฟังก์ชันหนึ่ง เช่น กดปุ่ม Start สั่งใช้งานฟังก์ชัน play() กดปุ่ม Options สั่งใช้งานฟังก์ชัน options()
#ส่วนตรงฟังก์ชัน play ก็จะมี pause_menu ด้วย ฟังก์ชัน options ก็คล้ายๆกันเลย

#-------------**หลักการ pause_menu อยู่ใน folder pausemenu เลย**----------------


def mainmenu():
    
    running = True
    while running:
        screen.blit(bg, (0,0))

        pygame.display.set_caption("cloneKnight")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
        




        if start_button.draw(screen):
            play()

        if options_button.draw(screen):
            options()

        if exit_button.draw(screen):
            running = False




        pygame.display.update()
    pygame.quit()



def play():


    game_pause = False
    menu_state = "main"

    resume_img = pygame.image.load("mainmenu + pausemenu/button_resume.png").convert_alpha()
    resume_button = button.Button(600, 80, resume_img, 1)

    options_img = pygame.image.load("mainmenu + pausemenu/button_options.png").convert_alpha()
    options_button = button.Button(600,180, options_img, 1)

    video_img = pygame.image.load("mainmenu + pausemenu/button_video.png").convert_alpha()
    video_button = button.Button(360,80, video_img, 1)

    audio_img = pygame.image.load("mainmenu + pausemenu/button_audio.png").convert_alpha()
    audio_button = button.Button(360,180, audio_img, 1)

    control_img = pygame.image.load("mainmenu + pausemenu/button_control.png").convert_alpha()
    control_button = button.Button(360,280, control_img, 1)

    back_img = pygame.image.load("mainmenu + pausemenu/button_back.png").convert_alpha()
    back_button = button.Button(360,380, back_img, 1)

    mainmenu_img = pygame.image.load("mainmenu + pausemenu/button_mainmenu.png").convert_alpha()
    mainmenu_button = button.Button(600,280, mainmenu_img, 1)

    exit_img = pygame.image.load("mainmenu + pausemenu/button_exit.png").convert_alpha()
    exit_button = button.Button(600,380, exit_img, 1)

    running = True
    while running:
        
        pygame.display.set_caption("cloneKnight_play")
        screen.fill((52,78,91))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_pause = True

            if event.type == pygame.QUIT:
                running = False

        if game_pause == True:
            if menu_state == "main":
                if resume_button.draw(screen):
                    game_pause = False
                if options_button.draw(screen):
                    menu_state = "options"
                if exit_button.draw(screen):
                    running = False
                if mainmenu_button.draw(screen):
                    mainmenu()
            if menu_state == "options":
                if video_button.draw(screen):
                    print("pass")
                if audio_button.draw(screen):
                    print("pass")
                if control_button.draw(screen):
                    print("pass")
                if back_button.draw(screen):
                    menu_state = "main"
        
        else:
            gen_text("This is the PLAY screen", font, WHITE, 360,240)




        pygame.display.update()
    pygame.quit()



def options():
    
    video_img = pygame.image.load("button_video.png").convert_alpha()
    video_button = button.Button(360,80, video_img, 1)

    audio_img = pygame.image.load("button_audio.png").convert_alpha()
    audio_button = button.Button(360,180, audio_img, 1)

    control_img = pygame.image.load("button_control.png").convert_alpha()
    control_button = button.Button(360,280, control_img, 1)

    back_img = pygame.image.load("button_back.png").convert_alpha()
    back_button = button.Button(360,380, back_img, 1)

    running = True
    while running:

        pygame.display.set_caption("cloneKnight_options")
        screen.fill((52,78,91))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                
        if video_button.draw(screen):
            print("pass")
        if audio_button.draw(screen):
            print("pass")
        if control_button.draw(screen):
            print("pass")
        if back_button.draw(screen):
            mainmenu()


        pygame.display.update()
    pygame.quit()


mainmenu()