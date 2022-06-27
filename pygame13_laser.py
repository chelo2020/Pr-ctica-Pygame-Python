import pygame, random

#ZONA DE CLASES

class meteoro(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load("images6.jpg").convert()
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()


class player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load("nave.jpg").convert()
		self.image.set_colorkey(white)
		self.rect=self.image.get_rect()
	def update(self):
		mouse_pos=pygame.mouse.get_pos()
		player.rect.x=mouse_pos[0]
		player.rect.y=410

class laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load("laser1.jpg").convert()
		self.image.set_colorkey(white)
		self.rect=self.image.get_rect()

	def update(self):
		self.rect.y+=5


white=(255,255,255)
black=(0,0,0)

pygame.init()

size=(700,500)

screem=pygame.display.set_mode(size)
clock=pygame.time.Clock()

done=False

score=0
all_sprite_list=pygame.sprite.Group()
meteor_lista=pygame.sprite.Group()
laser_lista=pygame.sprite.Group()

for i in range(50):
	meteor=meteoro()
	meteor.rect.x=random.randrange(680)
	meteor.rect.y=random.randrange(350)

	meteor_lista.add(meteor)
	all_sprite_list.add(meteor)


player=player()

all_sprite_list.add(player)




while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
		if event.type==pygame.MOUSEBUTTONDOWN:
			laser=laser()
			laser.rect.x=player.rect.x + 45
			laser.rect.y=player.rect.y - 20

			all_sprite_list.add(laser)
			laser_lista.add(laser)

	all_sprite_list.update()

	for laser in laser_lista:
		meteor_hit_list=pygame.sprite.spritecollide(laser,meteor_lista, True)
		for meteor in meteor_hit_list:
			all_sprite_list.remove(laser)
			laser_lista.remove(laser)
			score+=1
			if laser.rect.y<-10:
				all_sprite_list.remove(laser)
				laser_lista.remove(laser)


	screem.fill(white)
	all_sprite_list.draw(screem)


	pygame.display.flip()
	clock.tick(60)

pygame.quit()
