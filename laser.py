import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Laser(Sprite):
    '''a class to store laser properties and functions'''
    
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.ship = ship
        
        self.img = pygame.image.load('images/blaster.png')
        self.img = pygame.transform.scale(self.img, (50, 18))
        self.rect = self.img.get_rect()
        
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right
        
        #laser speed settings
        self.speed = 10
        
        #store the bullet's position as a decimal value
        self.x = float(self.rect.x)
        
    def update(self):
        '''move the bullets across the screen'''
        #update the decimal position of the bullet
        self.x += self.speed
        #update rect position
        self.rect.x = self.x
    
    def draw_laser(self):
        '''draw the bullet to the screen'''
        self.screen.blit(self.img, self.rect)
