import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
import sys


def run_game():
    #initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode(
		(1600, 800))
    pygame.display.set_caption('Type X')
    
    #start the main loop of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
run_game()

