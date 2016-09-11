#import ClockView
import pygame

class DigitalClockView():
    FONT_FAMILY = 'freesansbold.tff'
    FONT_SIZE = 32
    
    def __init__(self, clock, displaysurf):
        self.__clock = clock
        self.__dsiplaysurf = displaysurf
        self.__fontObj = pygame.font.Font(FONT_FAMILY, FONT_SIZE)

    def __drawDate(self):
        pass
        

    def __drawTime(self):
        pass
        
    def draw(self):
        self.__drawDate()
        self.__drawTime()
