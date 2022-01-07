import pygame
import time
import os
import random
#from playsound import playsound
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
        self.imag=pygame.image.load("assets/Gameover (1).png")
    def draw(self,window):
        window.blit(self.surface,(0,0))
    def draw_game_over(self,window):
        window.blit(self.imag,(0,0))


gameRunning = True
FPS=60
clock=pygame.time.Clock()
#creating our player

player=plane(7,window_w,window_h)
#creating our background
Background=background()

#creating our missile
Missi=missile(3,window_w,window_h, "assets/missile.png")
Missi2=missile(5,window_w,window_h, "assets/missile2.png")

# main game loop
collision=False

while gameRunning==True:
    clock.tick(FPS)
    ############################# User input #############################################
    for event in pygame.event.get():
        # quiting the game if user clicks quit
        if event.type == pygame.QUIT:
            gameRunning = False
    
            #Key Input
    key = pygame.key.get_pressed()
    if (key[pygame.K_LEFT] or key[pygame.K_a])and player.get_x()>0:
        player.move_LEFT()
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and player.get_x()<942:
        player.move_RIGHT()
    if (key[pygame.K_UP] or key[pygame.K_w]) and player.get_y()>0:
        player.moveDOWN()
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and player.get_y()<530:
        player.moveUP()
    if key[pygame.K_x]and collision==True:
        player.reset_to_defaultPosition(window_w,window_h)
        Missi.reset_Position(window_w,window_h)
        Missi2.reset_Position(window_w,window_h)
        collision=False
    if key[pygame.K_q]and collision==True:
        gameRunning=False

    ############################## updating our game before displaying it on window ##############################
    player.update()

    if(Missi.getRectM().colliderect(player.getRectP()) or Missi2.getRectM().colliderect(player.getRectP())):
        collision=True

    ############################## Displaying our updated settings on window ##############################
    if (collision == True):
        Background.draw_game_over(window)
    else:
        Missi.update(window_w, window_h, player.get_x(), 3, player.get_y())
        Missi2.update(window_w, window_h, player.get_x(), 5, player.get_y())
        Background.draw(window)
        player.draw(window)
        Missi.draw(window)
        Missi2.draw(window)
    ############################## Collison Detection ##############################
 
    pygame.display.update()
    
    #-------------------------------------------------------------------------------

# quiting pygame
#playsound('assets/audio.mp3')
pygame.quit()