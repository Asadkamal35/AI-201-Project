import pygame
import time
import os
import random
from Player import *
from Missile import *

# initializing pygame
pygame.init()

# creating the window for our game
window_w=1000
window_h=580
window = pygame.display.set_mode((window_w,window_h))

# setting title and icon for our game
pygame.display.set_caption("Missile Dodger")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

#class to display the background
class background:
    def __init__(self):
        self.surface=pygame.image.load("assets/background1.jpg")
    def draw(self,window):
        window.blit(self.surface,(0,0))


gameRunning = True
FPS=60
clock=pygame.time.Clock()
#creating our player
player=plane(7,window_w,window_h)
#creating our background
Background=background()
#creating our missile
Missi=missile(10,window_w,window_h)
# main game loop


while gameRunning:
    clock.tick(FPS)
    ############################# User input #############################################
    for event in pygame.event.get():
        # quiting the game if user clicks quit
        if event.type == pygame.QUIT:
            gameRunning = False
    #Key Input
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.get_x()>0:
        player.move_LEFT()
    if key[pygame.K_RIGHT] and player.get_x()<950:
        player.move_RIGHT()
    if key[pygame.K_UP] and player.get_y()>0:
        player.moveDOWN()
    if key[pygame.K_DOWN] and player.get_y()<550:
        player.moveUP()
    ###############################updating our game before displaying it on window ######################
    player.update()
    Missi.update(window_w,window_h)

    ############################## Displaying our updated settings on window ###############################################
    Background.draw(window)
    player.draw(window)
    Missi.draw(window)
    pygame.display.update()
    #-------------------------------------------------------------------------------

# quiting pygame
pygame.quit()