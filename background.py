import pygame

class Background():
    '''a class to manage the backgroud of the game and contain the scrolling function''' 

    def __init__(self, screen):
        #background one details
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.bg = pygame.image.load('images/bg_1.jpg')
        self.bg = pygame.transform.scale(self.bg, (1400, 800))
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.left = self.screen_rect.left
        self.bg_rect.center = self.screen_rect.center
        
        #background two details
        self.bg2 = pygame.image.load('images/bg_1.jpg')
        self.bg2 = pygame.transform.scale(self.bg2, (1400, 800))
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
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.bg2, self.bg2_rect)
