import pygame
from pygame.sprite import Sprite
import game_functions as gf

class Ship(Sprite):
	'''a class to manage the contents and settings of the ship'''
	
	def __init__(self, screen):
		super().__init__()
		#initialize ship attributes
		self.idle = pygame.image.load('images/ship_idle.png')
		self.up = pygame.image.load('images/sprite_10.png')
		self.down = pygame.image.load('images/sprite_02.png')
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		
		self.img = self.idle
		self.rect = self.img.get_rect()
		self.rect.left = self.screen_rect.left + 100
		self.rect.centery = self.screen_rect.centery
		
		# store a decimal value for the ship's center
		self.center_x = float(self.rect.centerx)
		self.center_y = float(self.rect.centery)
		
		#set ship flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		#set ship speed
		self.x_speed = 3
		self.y_speed = 5
		self.hp = 5
		
	def update(self, settings):
		if self.moving_right and self.rect.right < ((self.screen_rect.right /4)*3):
			self.center_x += self.x_speed
		if self.moving_left and self.rect.left > 0:
			self.center_x -= self.x_speed
		if self.moving_up and self.rect.top > 0:
			self.center_y -= self.y_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.y_speed
		self.rect.centerx = self.center_x
		self.rect.centery = self.center_y
		self.image_update()
		gf.check_hp(self, settings)
	
			
	def image_update(self):
		if self.moving_up and self.moving_down:
			self.img = self.idle
		elif self.moving_up:
			self.img = self.up
		elif self.moving_down:
			self.img = self.down
		else:
			self.img = self.idle
			
	def blitme(self):
		self.screen.blit(self.img, self.rect) 
		
	def damage(self, damage):
		self.hp -= damage
		print(str(self.hp))
