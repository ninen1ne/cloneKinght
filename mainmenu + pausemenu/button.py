#Make button class
#Cr. Coding With Russ

import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		w = image.get_width()
		h = image.get_height()
		self.image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#รับพิกัดจากเมาส์
		pos = pygame.mouse.get_pos()

		#เช็ตว่าพิกัดเมาส์อยู่ในขอบเขตของปุ่มไหม
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #[0] คือยังไม่ไกด 1 คือกดแล้ว
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		
		surface.blit(self.image, (self.rect))

		return action