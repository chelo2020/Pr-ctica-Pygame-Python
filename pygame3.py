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

	for x in range(100,700,100):#Realizamos el siguiente For para que nos recorra por cada cien pixeles.
		pygame.draw.rect(screen, black, (x,230,50,50))#Construimos un cuadrado dentor del ciclo for
		pygame.draw.line(screen, green, (x,0),(x,100),5)#Construimos una linea dentro del cilco for

	#Con esto actualizo mi pantalla
	pygame.display.flip()