import pygame
import sys
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from background import Background
from typex_settings import Settings
import time
from explosion import Explosion


clock = pygame.time.Clock()

#initialize pygame
pygame.init()

#create a screen object
screen = pygame.display.set_mode((1400, 800))
screen_rect = screen.get_rect()
pygame.display.set_caption('Type X')

def run_game():   
	#start the main loop of the game
	ship = Ship(screen)
	bg = Background(screen)
	lasers = Group()
	fighters = Group()
	mines = Group()
	settings = Settings()
	explosions = Group()
	
	while settings.game_active == True:
		gf.check_events(ship, screen, lasers)
		ship.update(settings)		
		gf.update_fighters(fighters, ship, screen_rect, explosions)
		gf.update_mines(mines, screen_rect, ship, explosions)
		gf.update_lasers(lasers, screen_rect, fighters, mines, explosions)
		explosions.update()
		bg.update()
		
		#draw the screen and ships/etc.
		gf.update_screen(bg, ship, fighters,  mines, lasers, explosions, screen)
		pygame.display.flip()
		gf.make_mob(fighters, mines, settings, screen)
		clock.tick(60) 
		
run_game()

