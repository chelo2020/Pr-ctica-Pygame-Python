import pygame, sys
pygame.init()#Iniciamos la programacion del juego

size=(800,500)

#Creamos una venta

screen=pygame.display.set_mode(size)

#Creamos nuestro bucle:

while True:
	for event in pygame.event.get():
		if event == pygame.QUIT:
			sys.exit()