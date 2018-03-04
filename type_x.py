import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite

theClock = pygame.time.Clock()

#initialize pygame
pygame.init()

#create a screen object
screen = pygame.display.set_mode((1600, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption('Type X')


#background one details
bg = pygame.image.load('images/bg_1.jpg')
bg_rect = bg.get_rect()
bg_rect.left = screen_rect.left
bg_rect.center = screen_rect.center

#background two details
bg2 = pygame.image.load('images/bg_1.jpg')
bg2_rect = bg2.get_rect()
bg2_rect.left = bg_rect.right
bg2_rect.top = bg_rect.top


class Ship():
    def __init__(self):
        self.img = pygame.image.load('images/ship_idle.png')
        self.rect = self.img.get_rect()
        self.rect.left = screen_rect.left + 100
        self.rect.centery = screen_rect.centery
    
    def update(self):
        screen.blit(self.img, self.rect) 


    
def run_game():   
    #start the main loop of the game
    ship = Ship()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        
        bg_rect.left -= 2
        bg2_rect.left -= 2
        
        if bg_rect.right == 0:
            bg_rect.left = bg2_rect.right
        
        if bg2_rect.right == 0:
            bg2_rect.left = bg_rect.right
        
        screen.blit(bg, bg_rect)
        screen.blit(bg2, bg2_rect)
        ship.update()
        
        pygame.display.flip()
        theClock.tick(2500)

run_game()

