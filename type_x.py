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



class Ship():
    '''a class to manage the contents and settings of the ship'''
    
    def __init__(self):
        #initialize ship attributes
        self.idle = pygame.image.load('images/ship_idle.png')
        self.up = pygame.image.load('images/sprite_10.png')
        self.down = pygame.image.load('images/sprite_02.png')
        
        self.img = self.idle
        self.rect = self.img.get_rect()
        self.rect.left = screen_rect.left + 100
        self.rect.centery = screen_rect.centery
        
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
        
    def update(self):
        if self.moving_right and self.rect.right < (screen_rect.right / 2):
            self.center_x += self.x_speed
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.x_speed
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.y_speed
        if self.moving_down and self.rect.bottom < screen_rect.bottom:
            self.center_y += self.y_speed
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
        self.image_update()
    
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
        screen.blit(self.img, self.rect) 

class Laser(Sprite):
    '''a class to store laser properties and functions'''
    
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.ship = ship
        
        self.img = pygame.image.load('images/blaster.png')
        self.img = pygame.transform.scale(self.img, (90, 18))
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

class Background():
    '''a class to manage the backgroud of the game and contain the scrolling function''' 

    def __init__(self):
        #background one details
        self.bg = pygame.image.load('images/bg_1.jpg')
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.left = screen_rect.left
        self.bg_rect.center = screen_rect.center
        
        #background two details
        self.bg2 = pygame.image.load('images/bg_1.jpg')
        self.bg2_rect = self.bg2.get_rect()
        self.bg2_rect.left = self.bg_rect.right
        self.bg2_rect.top = self.bg_rect.top
    
    def update(self):
        #update background position
        self.bg_rect.left -= 2
        self.bg2_rect.left -= 2
        #check the background and adjust if a gap appears
        if self.bg_rect.right == 0:
            self.bg_rect.left = self.bg2_rect.right
        if self.bg2_rect.right == 0:
            self.bg2_rect.left = self.bg_rect.right
    
    def blitme(self):
        screen.blit(self.bg, self.bg_rect)
        screen.blit(self.bg2, self.bg2_rect)

def check_events(ship, screen, lasers):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, screen, lasers, event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, screen, lasers, event)

def check_keydown_events(ship, screen, lasers, event):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        new_laser = Laser(screen, ship)
        lasers.add(new_laser)

def check_keyup_events(ship, screen, lasers, event):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False    

def update_lasers(lasers, screen_rect):
    lasers.update()
    for laser in lasers.sprites():
        if laser.rect.left > screen_rect.right:
            lasers.remove(laser)

def run_game():   
    #start the main loop of the game
    ship = Ship()
    bg = Background()
    lasers = Group()
    
    while True:
        check_events(ship, screen, lasers)
        
        bg.update()
        ship.update()
        update_lasers(lasers, screen_rect)
        
        #draw the screen and ships/etc.
        bg.blitme()
        ship.blitme()
        for laser in lasers.sprites():
            laser.draw_laser()
        
        pygame.display.flip()

run_game()

