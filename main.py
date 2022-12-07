#import the necessary libraries 
import pygame
import sys
from pygame.locals import *

#initialize pygame
pygame.init()

#create the window
WINDOW_SIZE = (800, 500)
window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Platformer')

#create the background
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((50,50,50))

#create the player
player = pygame.image.load('player.png').convert_alpha()
player_position = [0, 0]

#create the platforms
platforms = [[0,400,800,20],[300,350,200,20],[400,300,200,20],[200,250,200,20]]

#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player_position[0] -= 5
            if event.key == K_RIGHT:
                player_position[0] += 5
            if event.key == K_UP:
                player_position[1] -= 5
            if event.key == K_DOWN:
                player_position[1] += 5
           
    #collision detection
    for p in platforms:
        if player_position[1] + player.get_height() == p[1] and \
           player_position[0] + player.get_width() > p[0] and \
           player_position[0] < p[0] + p[2]:
            player_position[1] = p[1] - player.get_height()
    
    #draw the background
    window.blit(background, (0,0))
    
    #draw the platforms
    for p in platforms:
        pygame.draw.rect(background, (0,255,0), p)
    
    #draw the player
    window.blit(player, player_position)
    
    #update the window
    pygame.display.update()
