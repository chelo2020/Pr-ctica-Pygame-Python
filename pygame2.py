import pygame
import sys
pygame.init()#Iniciamos la programacion del juego

#Definimos Colores

black=(0,0,0)#Con este obtenemos el color negro
white=(255,255,255)#Con este obtenemos el color blanco
green=(0,255,0)#Con este obtenemos el color verde
red=(255,0,0)#Con este obtenemos el color rojo
blue=(0,0,255)#Con este obtenemos el color azul




size=(800,500)

#Creamos una venta

screen=pygame.display.set_mode(size)

#Creamos nuestro bucle:

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#Con esto le agrego color a la pantalla, siempre va primero
	screen.fill(white)
	###------Zona de dibujo
	pygame.draw.line(screen, green,[0,100],[100,300],5)#Construimos un linea horizontal
	pygame.draw.rect(screen, black,(100,100,80,80))#Construimos un cuadrado negro
	pygame.draw.circle(screen,black,(300,300),50)#Construimos un circulos
	###------zona d edibujo
	#Con esto actualizo mi pantalla
	pygame.display.flip()
