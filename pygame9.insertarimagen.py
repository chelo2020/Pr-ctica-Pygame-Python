import pygame

screem=pygame.display.set_mode([700,500])

clock=pygame.time.Clock()

done=False

#Insertamos una imagen a nuestro Juego, siempre debemos buscar 
#que la imagen tenga las mismas medidas que mi ventana

mund=pygame.image.load("pacman.jpg").convert()

#Bloque Principal

while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True

	#Para insertar una imagen por pantalla debemos usar el comando blit:

	screem.blit(mund,[0,0])

	pygame.display.flip()
	clock.tick(60)

pygame.quit()