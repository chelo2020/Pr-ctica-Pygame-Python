import pygame

screem=pygame.display.set_mode([700,500])

clock=pygame.time.Clock()

done=False

#Insertamos una imagen a nuestro Juego, siempre debemos buscar 
#que la imagen tenga las mismas medidas que mi ventana

mund=pygame.image.load("pacman.jpg").convert()
player=pygame.image.load("nave.jpg").convert()
pygame.mouse.set_visible(0)
player.set_colorkey([255,255,255])#Este metodo es para sacar el color que se encuentra alrededor de la imagen
#Bloque Principal

while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True

	mouse_pos=pygame.mouse.get_pos()
	x=mouse_pos[0]
	y=mouse_pos[1]

	#Para insertar una imagen por pantalla debemos usar el comando blit:

	screem.blit(mund,[0,0])
	screem.blit(player,[x,y])

	pygame.display.flip()
	clock.tick(60)

pygame.quit()