import pygame
from pygame.sprite import Sprite
from random import randint

class Fighter(Sprite):
	
	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('images/asteroid.png')
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.rect = self.image.get_rect()
		self.hp = 3
		self.rect.centerx = 1500
		self.rect.centery = randint(100, 700)
		self.speedx = randint(2,4)
		self.speedy = randint(-2,2)
	
	def update(self):
		self.rect.centerx -= self.speedx
		self.rect.centery += self.speedy
		
	def reset(self):
		self.rect.centerx = 1500
		self.rect.centery = randint(100, 700)
		self.speedx = randint(2,8)
		self.speedy = randint(-2,2) 
	
	def damage(self, damage):
		self.hp -= damage

	def blitme(self):
		self.screen.blit(self.image, self.rect)

