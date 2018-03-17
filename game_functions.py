import pygame
from laser import Laser
import sys
from random import randint
import math
import time
from mine import Mine
from fighter import Fighter
from explosion import Explosion

# KEYBOARD FUNCTIONS

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

#LASER FUNCTIONS

def update_lasers(lasers, screen_rect, fighters, mines, explosions):
    lasers.update()
    check_laser_collisions(lasers, fighters, mines)
    for laser in lasers.sprites():
        if laser.rect.left > screen_rect.right:
            lasers.remove(laser)

def check_laser_collisions(lasers, fighters, mines):
	for fighter in fighters:
		if pygame.sprite.spritecollideany(fighter, lasers):
			fighter.damage(1)
	collisions = pygame.sprite.groupcollide(lasers, fighters, True, False)
	
	for mine in mines:
		if pygame.sprite.spritecollideany(mine, lasers):
			mine.damage(1)
	collisions = pygame.sprite.groupcollide(lasers, mines, True, False)
 

# SHIP FUNCTIONS

def check_hp(ship, settings):
	if ship.hp <= 0:
		settings.game_active = False 


#FIGHTER FUNCTIONS

def update_fighters(fighters, ship, screen_rect, explosions):
	fighters.update()
	check_fighter_collisions(fighters, ship)
	for fighter in fighters.sprites():
		if fighter.hp == 0:
			explode = Explosion(fighter.rect.center)
			explosions.add(explode)
			fighters.remove(fighter)
		if fighter.rect.right < 0 or fighter.rect.bottom < 0 or fighter.rect.top > screen_rect.bottom:
			fighter.reset()
			
def check_fighter_collisions(fighters, ship):
	for fighter in fighters.sprites():
		if pygame.sprite.collide_rect(fighter, ship):
			ship.damage(1)
			fighters.remove(fighter)

#MINE FUNCTIONS

def update_mines(mines, screen_rect, ship, explosions):
	check_movement(mines, ship)
	check_mines_collisions(mines, ship)
	for mine in mines.sprites():
		if mine.hp <= 0:
			detonate(mines, mine, ship)
			s_distance = check_distance(ship,mine)
			if s_distance < 100:
				ship.damage(1)
			explode = Explosion(mine.rect.center)
			explosions.add(explode)
			mines.remove(mine)
		if mine.rect.right < 0:
			mines.remove(mine)

def detonate(mines, mine, ship):
	for m in mines:
		m_distance = check_distance(m, mine)
		if m_distance < 100:
			m.hp = 0
		
		
def check_movement(mines, ship):
	for mine in mines.sprites():
		dist = check_distance(mine, ship)
		if dist < 200:
			attract(mine, ship)
		else:
			mine.update()

def check_distance(mine, ship):
	p1 = [mine.rect.centerx, mine.rect.centery]
	p2 = [ship.rect.centerx, ship.rect.centery]
	distance = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) )
	return distance

def attract(mine, ship):
	x_update(mine, ship)
	y_update(mine, ship)		
	
def x_update(mine, ship):
	if mine.rect.centerx < ship.rect.centerx:
		mine.rect.centerx += 2
	elif mine.rect.centerx > ship.rect.centerx:
		mine.rect.centerx -= 2
		
def y_update(mine, ship):
	if mine.rect.centery < ship.rect.centery:
		mine.rect.centery += 2
	elif mine.rect.centery > ship.rect.centery:
		mine.rect.centery -= 2
		
def check_mines_collisions(mines, ship):
	for mine in mines.sprites():
		if pygame.sprite.collide_rect(mine, ship):
			ship.damage(1)
			mine.hp=0		

#SCREEN UPDATES

def update_screen(bg, ship, fighters, mines, lasers, explosions, screen):
	bg.blitme()
	ship.blitme()
		
	for fighter in fighters.sprites():
		fighter.blitme()
		
	for mine in mines.sprites():
		mine.blitme()
		
	for laser in lasers.sprites():
		laser.draw_laser()
	
	explosions.draw(screen)

#SPAWNING MOB SETTINGS

def make_mob(fighters, mines, settings, screen):
	current_time = pygame.time.get_ticks()
	interval = current_time - settings.last_time
	spawn = randint(0,3)
	if (len(fighters) + len(mines)) < settings.mob_size:
		if interval > settings.delay:
			if spawn == 1:
				new_fighter = Fighter(screen)
				fighters.add(new_fighter)
			if spawn == 2:
				spawn_mines(mines, screen)
			settings.last_time = current_time

def spawn_mines(mines, screen):
	y = randint(100, 700)
	new_y = y
	x = 1500
	new_mine = Mine(screen, x, y)
	mines.add(new_mine)
	
	for numbers in range(0,4):
		new_y+=50
		new_mine = Mine(screen, x, new_y)
		mines.add(new_mine)
		if new_y > 1400 or new_y < 0:
			new_y = y
			x+=100
		
			
	
	
	
	


