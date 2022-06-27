import pygame, random, sys

SCREEM_WIDTH=700 
SCREEM_HEIGHT=500 
black=(0,0,0) 
white=(255,255,255)

class meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load("pelota1.jpg").convert()
		self.image.set_colorkey(white)
		self.rect=self.image.get_rect()

	def update(self):
		self.rect.y+=1

		if self.rect.y>SCREEM_HEIGHT:
			self.rect.y=-10
			self.rect.x=random.randrange(SCREEM_HEIGHT)

class player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=pygame.image.load("nave1.jpg").convert()
		self.image.set_colorkey(white)
		self.rect=self.image.get_rect()

	def update(self):
		mouse_pos=pygame.mouse.get_pos()
		self.rect.x=mouse_pos[0]
		self.rect.y=mouse_pos[1]

class Game(object):
	def __init__(self):
		self.Game_over=False

		self.score=0

		self.meteoro_lista=pygame.sprite.Group()
		self.all_sprite_lista=pygame.sprite.Group()

		for i in range(50):
			meteoro = meteor()
			meteoro.rect.x=random.randrange(700)
			meteoro.rect.y=random.randrange(500)

			self.meteoro_lista.add(meteoro)
			self.all_sprite_lista.add(meteoro)

		self.player=player()
		self.all_sprite_lista.add(self.player)

	def proceso_evento(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				return True
		return False

		if event.type==pygame.MOUSEBUTTONDOWN:
			if self.Game_over:
				self.__init__()

	def la_logica(self):

		if not self.Game_over:

			self.all_sprite_lista.update()

			meteoro_hit_list=pygame.sprite.spritecollide(self.player,self.meteoro_lista, True)

			for meteoro in meteoro_hit_list:
				self.score +=1
				print(self.score)

			if len(self.meteoro_lista)==0:
				self.Game_over=True


	def display(self,screem):
		screem.fill(white)

		if self.Game_over:
			font=pygame.font.SysFont("time new roman", 50)
			text=font.render("Game_over, has un clic para continuar", True, black )
			center_x=(SCREEM_WIDTH//2)-(text.get_width()//2)
			center_y=(SCREEM_HEIGHT//2)-(text.get_height()//2)
			screem.blit(text,[center_x,center_y])


		if not self.Game_over:
			self.all_sprite_lista.draw(screem)
		

		pygame.display.flip()


def main():
	pygame.init()

	screem=pygame.display.set_mode([SCREEM_WIDTH,SCREEM_HEIGHT])

	done=False

	clock=pygame.time.Clock()

	game=Game()

	while not done:
		done=game.proceso_evento()
		game.la_logica()
		game.display(screem)
		clock.tick(60)
	pygame.quit()


if __name__ =="__main__":
	main()
