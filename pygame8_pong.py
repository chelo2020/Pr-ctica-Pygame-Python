
import pygame

pygame.init()

black=(0,0,0)
white=(255,255,255)

size=(700,500)
player_width=15
player_height=90

screem=pygame.display.set_mode(size)
clock=pygame.time.Clock()
#Coordenadas y velocidad del jugador 1
jugardor1_x_coor=50
jugador1_y_coor=300-45
jugardor1_y_speed=0
#Coordenadas y velocidad del jugador 1
jugardor2_x_coor=700- player_width
jugador2_y_coor=300-45
jugardor2_y_speed=0
#coordenadas y velocidad de la pelota
pelota_x=350
pelota_y=250
pelota_speed_x=3
pelota_speed_y=3




game_over=False

while not game_over:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			game_over=True
		if event.type==pygame.KEYDOWN:
			#JUGADOR 1
			if event.key==pygame.K_w:
				jugardor1_y_speed=-3
			if event.key==pygame.K_s:
				jugardor1_y_speed=3
			#JUGADOR 2
			if event.key==pygame.K_UP:
				jugardor2_y_speed=-3
			if event.key==pygame.K_DOWN:
				jugardor2_y_speed=3
		if event.type==pygame.KEYUP:
			#JUGADOR 1
			if event.key==pygame.K_w:
				jugardor1_y_speed=0
			if event.key==pygame.K_s:
				jugardor1_y_speed=0
			#JUGADOR 2
			if event.key==pygame.K_UP:
				jugardor2_y_speed=0
			if event.key==pygame.K_DOWN:
				jugardor2_y_speed=0

	if pelota_x >590 or pelota_x<10:
		pelota_speed_y*=-1

	#revisa si la pelota sale por el lado derecho

	if pelota_x>700:
		pelota_x=350
		pelota_y=250
		#si sale de la pantalla invierte la direccion
		pelota_speed_x*=-1
		pelota_speed_y*=-1
	#revisa si la pelota sale por el lado izquierdo

	if pelota_x<0:
		pelota_x=350
		pelota_y=250
		#si sale de la pantalla invierte la direccion
		pelota_speed_x*=-1
		pelota_speed_y*=-1
		




	#MODIFICA LAS COORDENADAS PARA DAR MOV. A LOS JUGADORES/PELOTA
	jugador1_y_coor+=jugardor1_y_speed
	jugador2_y_coor+=jugardor2_y_speed
	#movimiento pelota
	pelota_x+=pelota_speed_x
	pelota_y+=pelota_speed_y


	screem.fill(black)

	#Zona de Dibujo

	jugardor1=pygame.draw.rect(screem,white,(jugardor1_x_coor,jugador1_y_coor,player_width,player_height))
	jugador2=pygame.draw.rect(screem,white,(jugardor2_x_coor,jugador2_y_coor,player_width,player_height))
	pelota=pygame.draw.circle(screem,white,(pelota_x,pelota_y),10)
		
	#Colisiones entre la pelota y el Jugador
	if pelota.colliderect(jugardor1) or pelota.colliderect(jugador2):
		pelota_speed_x*=-1
		
	pygame.display.flip()
	clock.tick(60)

pygame.quit()



