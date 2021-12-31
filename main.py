import pygame
import time
import os
import random
from Player import *

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

#Missle Added
missle=pygame.image.load(os.path.join('assets/missile.png'))
missle=pygame.transform.scale(missle,(20,40))
missle_x=random.randint(0,1000)
missle_y=580

gameRunning = True
FPS=60
clock=pygame.time.Clock()
#creating our player
player=plane(5,window_w,window_h)
#creating our background
Background=background()
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
        player.moveDOWN()
    ###############################updating our game before displaying it on window ######################
    player.update()
    missle_y = missle_y - 5
    ############################## Displaying our updated settings on window ###############################################
    Background.draw(window)
    player.draw(window)
    window.blit(missle,(missle_x,missle_y))
    pygame.display.update()
    #-------------------------------------------------------------------------------

# quiting pygame
pygame.quit()