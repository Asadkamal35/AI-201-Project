import pygame

class plane:
    def __init__(self,speed,window_w,window_h):
        self.__surface=pygame.transform.scale(pygame.image.load("assets/plane.png"),size=(55,44))
        self.__Rect=self.__surface.get_rect()
        #to center initial position of our window
        self.__Rect.x=window_w/2
        self.__Rect.y=window_h/2
        self.__speed=speed
        self.__move_up,self.__move_down,self.__move_left,self.__move_right=False,False,False,False
    #to move player rectangle up
    def moveUP(self):
        self.__move_up=True

    # to move player rectangle down
    def moveDOWN(self):
        self.__move_down=True

    # to move player rectangle left
    def move_LEFT(self):
        self.__move_left=True

    # to move player rectangle right
    def move_RIGHT(self):
        self.__move_right=True
    #to get current x co-ordinate of our player
    def get_x(self):
        return self.__Rect.x
    #to get current x co-ordinate of our player
    def get_y(self):
        return self.__Rect.y
    #to get speed of our player
    def get_speed(self):
        return self.__speed
    #to reset all the movements of our player
    def reset_movement(self):
        self.__move_right,self.__move_left,self.__move_up,self.__move_down=False,False,False,False
    #method to update the location of our player after every user input
    def update(self):
        if self.__move_up==True:
            self.__Rect.y+=self.__speed
        elif self.__move_down==True:
            self.__Rect.y-=self.__speed
        elif self.__move_left==True:
            # flipping the image when the user starts to move right
            tempsurface=self.__surface=pygame.transform.scale(pygame.image.load("assets/plane.png"),size=(55,44))
            temprect=tempsurface.get_rect()
            temprect.x,temprect.y=self.__Rect.x,self.__Rect.y
            self.__Rect=temprect
            self.__Rect.x-=self.__speed
        elif self.__move_right==True:
            #flipping the image when the user starts to move right
            tempsurface=self.__surface=pygame.transform.scale(pygame.image.load("assets/planeflip.png"),size=(55,44))
            temprect=tempsurface.get_rect()
            temprect.x,temprect.y=self.__Rect.x,self.__Rect.y
            self.__Rect=temprect
            self.__Rect.x+=self.__speed
        self.reset_movement()
    #method to display the image on our window
    def draw(self,Window):
        Window.blit(self.__surface,self.__Rect)
