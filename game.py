import os
import sys
import pygame as pg
import pygame.image as pgImage
import pygame.transform as pgTransf
import pygame.time as pgTime
import pygame.mouse as pgMouse
import pygame.event as pgEvent
import pygame.display as pgDisplay
from viewport import Viewport

class Game:
    def __init__(self, width, heigth):
        self.black = pg.Color(0, 0, 0)
        self.red = pg.Color(255, 0, 0)
        self.pink = pg.Color(255, 0, 255)
        
        self.clock = pgTime.Clock()
        self.targetFps : int = 60

        self.viewport = Viewport(width, heigth, self.pink)

    def loop(self):
        keep : bool = True
        while keep:
            self.clock.tick(self.targetFps)
            self.viewport.screen.fill(self.black)

            frameTime : float = self.clock.get_fps()
            frameRate : int = int(frameTime if frameTime > 0 else 0)

            self.viewport.debug()
            self.viewport.visualDebug.reset()

            for event in pgEvent.get():
                if (event.type == pg.QUIT):
                    keep = False
                self.viewport.handleEvent(event)
                
            pgDisplay.flip()
        pg.quit()