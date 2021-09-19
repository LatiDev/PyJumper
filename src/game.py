import os
import sys
import copy
import pygame as pg
import pygame.image as pgImage
import pygame.transform as pgTransf
import pygame.time as pgTime
import pygame.mouse as pgMouse
import pygame.event as pgEvent
import pygame.display as pgDisplay
from levelmanager import *
from viewport import *
from assetmanager import *
from level import *
from spritesheetterrain import *
from viewportsettingschangedevent import *
from utils import *

class Game:
    def __init__(self, width, heigth):
        self.black = pg.Color(0, 0, 0)
        self.red = pg.Color(255, 0, 0)
        self.pink = pg.Color(255, 0, 255)
        
        self.clock = pgTime.Clock()
        self.targetFps : int = 60

        SpriteSheetTerrain.load("GrassBlockTileSet.png", (16, 16), PROCESS_TERRAIN, GRASS_RGB)
        SpriteSheetTerrain.load("MidBrickTileSet.png", (16, 16), PROCESS_TERRAIN, BRICK_RGB)
        SpriteSheetTerrain.load("SmallPikeBlockTileSet.png", (16, 16), PROCESS_TERRAIN, PIKE_RGB)
        SpriteSheet.load("CharacterTileSet.png", (16, 16), PROCESS_ACTOR, PLAYER_RGB)

        self.viewport = Viewport(width, heigth, self.pink)
        self.levelMngr = LevelManager((width, heigth))

        self.viewport.vpChanged.add(Event(self.levelMngr.onViewportChanged, 3))

    def debug(self):
        self.viewport.visualDebug.display(f"{int(self.clock.get_fps())}Fps", self.red)
        self.viewport.visualDebug.display(f"{pgMouse.get_pos()}", self.red)

    def loop(self):
        keep : bool = True
        while keep:
            self.clock.tick(self.targetFps)
            self.viewport.screen.fill(self.black)
            self.viewport.screen.blit(self.levelMngr.curlvlScaled.level, (0, 0))

            #frameTime : float = self.clock.get_fps()
            #frameRate : int = int(frameTime if frameTime > 0 else 0)

            self.debug()
            self.viewport.visualDebug.space()
            self.viewport.debug()            
            self.viewport.visualDebug.reset()

            #self.viewport.screen.blit(self.grassTest.tiles[0], (0, 0))

            for event in pgEvent.get():
                if (event.type == pg.QUIT):
                    keep = False
                if event.type == pg.KEYDOWN:
                    if (event.key == pg.K_g):
                        self.levelMngr.gotToLevel(-1)
                    if (event.key == pg.K_h):
                        self.levelMngr.gotToLevel(1)
                self.viewport.handleEvent(event)
                

            pgDisplay.flip()
        pg.quit()