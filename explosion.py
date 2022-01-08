import pygame

class explosion:
    def __init__(self):
       self.__surface=pygame.transform.scale(pygame.image.load("assets/smoke1.png"),size=(60,90))
       self.__Rect=self.__surface.get_rect()
    
    def reset_position(self):
        self.__Rect.y=-5000

    def draw(self,window,x,y):
        self.__Rect.x=x
        self.__Rect.y=y
        window.blit(self.__surface,self.__Rect)