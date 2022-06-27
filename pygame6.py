import pygame
import sys

pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

size=(800,500)
screem=pygame.display.set_mode(size)
clock=pygame.time.Clock()


pygame.mouse.set_visible(0)#Cuando le inserto un 0 es porque no quiero ver el mouse movimendo mi pantalla

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

	mouse_pos=pygame.mouse.get_pos()
	x=mouse_pos[0]
	y=mouse_pos[1]
	screem.fill(white)


	pygame.draw.rect(screem, red, (x,y,100,100))
	pygame.display.flip()
	clock.tick(60)


