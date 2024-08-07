#Run This File
#Cr. Coding With Russ

import pygame
import button

pygame.init()

#ตั้งค่าขนาดหน้าจอ
pygame.display.set_caption("cloneKnight")
SCREEN_H = 480
SCREEN_W = 720
screen = pygame.display.set_mode((SCREEN_W , SCREEN_H))



game_pause = False
menu_state = "main"

# line 19-40 --- ใส่รูปภาพ
resume_img = pygame.image.load("pausemenu/button_resume.png").convert_alpha() #convert_alpha() = ทำให้สามารถใช้งานภาพที่มีความโปร่งใสได้อย่างมีประสิทธิภาพ
resume_button = button.Button(360, 140, resume_img, 1)

options_img = pygame.image.load("pausemenu/button_options.png").convert_alpha()
options_button = button.Button(360,240, options_img, 1)

video_img = pygame.image.load("pausemenu/button_video.png").convert_alpha()
video_button = button.Button(360,80, video_img, 1)

audio_img = pygame.image.load("pausemenu/button_audio.png").convert_alpha()
audio_button = button.Button(360,180, audio_img, 1)

control_img = pygame.image.load("pausemenu/button_control.png").convert_alpha()
control_button = button.Button(360,280, control_img, 1)

back_img = pygame.image.load("pausemenu/button_back.png").convert_alpha()
back_button = button.Button(360,380, back_img, 1)

exit_img = pygame.image.load("pausemenu/button_exit.png").convert_alpha()
exit_button = button.Button(360,340, exit_img, 1)

font = pygame.font.SysFont("komikaaxis", 40)
color = (255,255,255)

#ฟังก์ชันสร้าง text เฉยๆ
def gen_text(text, font, color, x, y):
    img = font.render(text, True , color)
    img_rect = img.get_rect(center=(x,y)) #(center=(x,y)) คือให้นับพิกัดจากตรงกลางข้อความ ไม่ใช่ขอบด้านซ้ายบน
    screen.blit(img, (img_rect))

running = True
while running:

    screen.fill((0,0,0))

    
    for event in pygame.event.get():
        #ตรวจจับว่ามีการกดปุ่ม ESC ไหม
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True
        if event.type == pygame.QUIT:
            running = False

    #Pause menu
    if game_pause == True:
        if menu_state == "main":
            if resume_button.draw(screen):
                game_pause = False
            if options_button.draw(screen):
                menu_state = "options" #ให้ทำงานในบรรทัดที่ 69
            if exit_button.draw(screen):
                running = False

        #เมื่อกดปุ่ม Options
        if menu_state == "options":
            if video_button.draw(screen):
                print("pass")
            if audio_button.draw(screen):
                print("pass")
            if control_button.draw(screen):
                print("pass")
            if back_button.draw(screen):
                menu_state = "main" #ให้ย้อนกลับไปหน้าที่มี resume options exit
    else:
        gen_text("Press ESC to pause", font, color,360,240)

    
    pygame.display.update()

pygame.quit()