import pygame, random


white=(255,255,255)
black=(0,0,0)

#Creamos una clase para el meteoro:
class Meteor(pygame.sprite.Sprite):
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

pygame.init()

screem=pygame.display.set_mode([700,500])

clock=pygame.time.Clock()

done=False

score=0

pygame.mouse.set_visible(0)

#Insertamos una imagen a nuestro Juego, siempre debemos buscar 
#que la imagen tenga las mismas medidas que mi ventana


meteor_lista=pygame.sprite.Group()
all_sprite_lista=pygame.sprite.Group()

for i in range(50):
	meteor = Meteor()
	meteor.rect.x=random.randrange(700)
	meteor.rect.y=random.randrange(500)

	meteor_lista.add(meteor)
	all_sprite_lista.add(meteor)

player=player()
all_sprite_lista.add(player)
while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True

	mouse_pos= pygame.mouse.get_pos()
	player.rect.x=mouse_pos[0]
	player.rect.y=mouse_pos[1]

	meteor_hit_list=pygame.sprite.spritecollide(player,meteor_lista, True)

	for meteor in meteor_hit_list:
		score+=1
		


	#Para insertar una imagen por pantalla debemos usar el comando blit:

	screem.fill(white)

	all_sprite_lista.draw(screem)

	

	pygame.display.flip()
	clock.tick(60)

pygame.quit()