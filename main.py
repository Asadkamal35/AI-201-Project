import pygame
import time
import os

# initializing pygame
pygame.init()


# created the window for our game
window = pygame.display.set_mode((1000,580))

# setting title and icon for our game
pygame.display.set_caption("Missile Dodger")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# loading background
background = pygame.image.load(os.path.join("background.PNG")).convert()
#Player created
helicopter=pygame.image.load('helicopter.png').convert()
helicopter=pygame.transform.scale(helicopter,(55,44))
rotate=0
player_x=500
player_y=300

gameRunning = True
FPS=60
clock=pygame.time.Clock()
# main game loop


while gameRunning:
    clock.tick(FPS)
    #########################Displaying our background on window #####################################
    window.fill((255, 255, 255))
    window.blit(background,(0,0))
    helicopter=pygame.image.load(os.path.join('helicopter.png'))
    helicopter=pygame.transform.scale(helicopter,(55,44))
    ############################# checking for user input #############################################
    for event in pygame.event.get():
        # quiting the game if user clicks quit
        if event.type == pygame.QUIT:
            gameRunning = False
    #Key Input
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player_x>0:
        helicopter = pygame.transform.rotate(helicopter,(rotate+5))
        player_x=player_x-5
    if key[pygame.K_RIGHT] and player_x<980:
        helicopter = pygame.transform.flip(helicopter,True,False)
        helicopter = pygame.transform.rotate(helicopter,(rotate-5))
        player_x=player_x+5
    if key[pygame.K_UP] and player_y>0:
        player_y=player_y-5
    if key[pygame.K_DOWN] and player_y<550:
        player_y=player_y+5       
    ##############################Updating our window ###############################################
    window.blit(helicopter,(player_x,player_y))
    pygame.display.update()
    #-------------------------------------------------------------------------------

# quiting pygame
pygame.quit()