import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Mine(Sprite):
	'''a class to store mines'''
	
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		
		self.image = pygame.image.load('images/mine.png')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.hp = 3
		self.rect.centerx = 1500
		self.rect.centery = randint(100, 700)
		self.speedx = 1
	
	def update(self):
		self.rect.centerx -= self.speedx
	
	def reset(self):
		self.rect.centerx = 1500
		self.rect.centery = randint(100, 700)
	
	def damage(self, damage):
		self.hp -= damage

	def blitme(self):
		self.screen.blit(self.image, self.rect)
	
