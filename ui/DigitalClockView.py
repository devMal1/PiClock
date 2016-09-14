#import ClockView
import pygame

class DigitalClockView():
    
    def __init__(self, clock, displaysurf):
        self.__clock = clock
        self.__displaysurf = displaysurf

    def __draw(self, text, fontSize, xOffset, yOffset):
        FONT_FAMILY = "comicsansms"
        TEXT_COLOR = (255, 160, 20)
        BG_COLOR = (0, 0, 0)
        fontObj = pygame.font.SysFont(FONT_FAMILY, fontSize)
        textSurfaceObj = fontObj.render(text, True, TEXT_COLOR, BG_COLOR)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (self.__displaysurf.get_width()/2 + xOffset,
                              self.__displaysurf.get_height()/2 + yOffset)
        self.__displaysurf.blit(textSurfaceObj, textRectObj)
        
    def draw(self):
        MARGIN = 20
        #time
        time = self.__clock.timeNow()
        T_TEXT = time.strftime("%I:%M")
        T_FONTSIZE = 200
        T_XOFFSET = 0
        T_YOFFSET = 0
        self.__draw(T_TEXT, T_FONTSIZE, T_XOFFSET, T_YOFFSET)
        
        #time of day
        ampmString = time.strftime("%p")
        fontSize = 20
        xOffset =   round( (fontSize * 2 /3) + T_FONTSIZE * 2 / 3)
        yOffset = round( (fontSize * 2 / 3) + T_FONTSIZE / 4 )
        self.__draw(ampmString, fontSize, xOffset, yOffset) 

        #date
        dateString = self.__clock.dateNow().strftime("%m.%d.%Y")
        fontSize = round(T_FONTSIZE / 4)
        xOffset = 0
        yOffset = round( (T_FONTSIZE / 2) +  MARGIN)
        self.__draw(dateString, fontSize, xOffset, yOffset)
