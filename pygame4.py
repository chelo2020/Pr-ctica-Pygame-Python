
#importamos funciones

import pygame
import sys
pygame.init()#Iniciamos la programacion del juego

#Definimos Colores

black=(0,0,0)#Con este obtenemos el color negro
white=(255,255,255)#Con este obtenemos el color blanco
green=(0,255,0)#Con este obtenemos el color verde
red=(255,0,0)#Con este obtenemos el color rojo
blue=(0,0,255)#Con este obtenemos el color azul


#Le damos el ancho que queremos en nuestra pantalla

size=(800,400)

#Creamos una venta

screen=pygame.display.set_mode(size)

#Nos permite controlar la velocidad de nuestro objeto
clock=pygame.time.Clock()

#Coordenadas del cuadrado
cord_x=300
cord_y=100

#Creamos la velocidad del cuadrado

speed_x=3
speed_y=3

#Creamos nuestro bucle:

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# estos codigos controlan nuestro movimiento dentro de la pantalla
	#LOGICA DEL PROGRAMA
	if cord_x>720 or cord_x<0:
		speed_x*=-1

	if cord_y>320 or cord_y<0:
		speed_y*=-1
	#LOGICA DEL PROGRAMA

	# Con este codigo le pongo animacion a mi objeto
	cord_x += speed_x
	cord_y += speed_y


	#Con esto le agrego color a la pantalla, siempre va primero
	screen.fill(white)
	###------Zona de dibujo
	pygame.draw.rect(screen, red,(cord_x,cord_y,80,80))
	
	#zona de Dibujo

	#Con esto actualizo mi pantalla
	pygame.display.flip()
	clock.tick(60)#Este parametro nos da la velocidad que le queremos implementar a nuestros objetos




