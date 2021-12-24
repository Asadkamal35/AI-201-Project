import pygame

# initializing pygame
pygame.init()


# created the window for our game
window = pygame.display.set_mode((1000,580))

# setting title and icon for our game
pygame.display.set_caption("Missile Dodger")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# loading background
background = pygame.image.load("background.PNG")

gameRunning = True

# main game loop
while gameRunning:
    #########################Displaying our background on window #####################################
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    ############################# checking for user input #############################################
    for event in pygame.event.get():
        # quiting the game if user clicks quit
        if event.type == pygame.QUIT:
            gameRunning = False
    ##############################Updating our window ###############################################
    pygame.display.update()
    #-------------------------------------------------------------------------------

# quiting pygame
pygame.quit()