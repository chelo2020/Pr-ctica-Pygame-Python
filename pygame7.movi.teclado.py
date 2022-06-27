import pygame
import sys

pygame.init()

black=(0,0,0)
red=(255,0,0)
white=(255,255,255)

size=(700,400)

screem=pygame.display.set_mode(size)
clock=pygame.time.Clock()

#Coordenadas del cuadrado
coord_x=10
coord_y=10

#velocidad del cuadrado

x_speed=0
y_speed=0

pygame.mouse.set_visible(0)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		#Eventos teclado
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_speed=-3
			if event.key==pygame.K_RIGHT:
				x_speed=3

			if event.key==pygame.K_UP:
				y_speed=-3
			if event.key==pygame.K_DOWN:
				y_speed=3 

		if event.type == pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				x_speed=0
			if event.key==pygame.K_RIGHT:
				x_speed=0
			if event.key==pygame.K_UP:
				y_speed=0
			if event.key==pygame.K_DOWN:
				y_speed=0


	screem.fill(white)

	coord_x+=x_speed
	coord_y+=y_speed

	pygame.draw.rect(screem, red, (coord_x,coord_y,100,100))
	pygame.display.flip()
	clock.tick(60)