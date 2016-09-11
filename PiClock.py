import models.Clock, ui.DigitalClockView
import pygame, sys
from pygame.locals import *

#GLOBAL CONSTANTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
BG_COLOR = (255, 160, 20)
FPS = 15 #frames per second

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('PiClock')

    sysClock = models.Clock.Clock()
    clockView = ui.DigitalClockView.DigitalClockView(sysClock, DISPLAYSURF)
    
    while True: #game loop
        DISPLAYSURF.fill(BG_COLOR)
        clockView.draw()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
