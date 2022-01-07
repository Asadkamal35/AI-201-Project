import pygame
import random
from playsound import playsound

class missile:

    def __init__(self,speed,window_w,window_h):
        #playsound('assets/audio.mp3')
        #Creating a missile and passing it in a rectangle
        self.__surface=pygame.transform.scale(pygame.image.load("assets/missile.png"),size=(15,40))
        self.__Rect=self.__surface.get_rect()
        self.__Rect.x=random.randint(0,window_w)
        self.__Rect.y=window_h
        self.__speed=speed
    def getRectM(self):
        return self.__Rect
    def get_x(self):
        return self.__Rect.x

    def get_y(self):
        return self.__Rect.y

    def update(self,w,h,player_x,missi_spped):
        if player_x < self.__Rect.x:
            self.__Rect.x = self.__Rect.x-missi_spped
        elif(player_x > self.__Rect.x):
           self.__Rect.x = self.__Rect.x+missi_spped
        if self.__Rect.y<-50:
            self.__Rect.x=random.randint(0,w)#here should come the best move for computer
            self.__Rect.y=h
        else:
            self.__Rect.y-=self.__speed
    def reset_Position(self,window_w,window_h):
        self.__Rect.x=random.randint(0,window_w)
        self.__Rect.y=window_h
    def draw(self,Window):
        Window.blit(self.__surface,self.__Rect)