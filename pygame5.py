
import pygame
import sys

pygame.init()


size=(800,500)

white=(255,255,255)
red=(255,0,0)



screen=pygame.display. set_mode(size)
clock=pygame.time.Clock()

coord_list=[]
for i in range(60):
		x=random.randint(0,800)
		y=random.randint(0,500)
		coord_list.append([x,y])
		

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


	screen.fill(white)

	for coord in coord_list:
		x=j[0]
		y=j[1]
		pygame.draw.circle(screen,red,coord,2)
		coord[1]+=1
		if coord[1]>500:
			coord[1]=0


	screen.fill(white)
	pygame.display.flip()
	clock.tick(30)