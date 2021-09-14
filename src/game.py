import os
import sys
import pygame as pg
import pygame.image as pgImage
import pygame.transform as pgTransf
import pygame.time as pgTime
import pygame.mouse as pgMouse
import pygame.event as pgEvent
import pygame.display as pgDisplay
from viewport import *
from assetmanager import *
from level import *
from spritesheetterrain import *
from viewportsettingschangedevent import *

class Game:
    def __init__(self, width, heigth):
        self.black = pg.Color(0, 0, 0)
        self.red = pg.Color(255, 0, 0)
        self.pink = pg.Color(255, 0, 255)
        
        self.clock = pgTime.Clock()
        self.targetFps : int = 60

        self.viewport = Viewport(width, heigth, self.pink)
        self.assetMngr = AssetManager()

        grassImg = self.assetMngr.loadAsset(AssetManager.SPRITESHEET_PATH, "GrassBlockTileSet.png")
        brickImg = self.assetMngr.loadAsset(AssetManager.SPRITESHEET_PATH, "MidBrickTileSet.png")
        smallPikeImg = self.assetMngr.loadAsset(AssetManager.SPRITESHEET_PATH, "SmallPikeBlockTileSet.png")
        characterImg = self.assetMngr.loadAsset(AssetManager.SPRITESHEET_PATH, "CharacterTileSet.png")

        SpriteSheetTerrain(grassImg, (16, 16), PROCESS_TERRAIN, GRASS_RGB)
        SpriteSheetTerrain(brickImg, (16, 16), PROCESS_TERRAIN, BRICK_RGB)
        SpriteSheetTerrain(smallPikeImg, (16, 16), PROCESS_TERRAIN, PIKE_RGB)
        SpriteSheet(characterImg, (16, 16), PROCESS_ACTOR, PLAYER_RGB)

        levelZeroImg = self.assetMngr.loadAsset(AssetManager.LEVEL_PATH, f"lvl{0}.bmp")

        self.levelZero = Level(levelZeroImg)

        grassTest : SpriteSheetTerrain = SpriteSheet.ALL[1]
        self.grass16 : pg.Surface = grassTest.tiles[0]
        self.grass32 = grassTest.scaleTileTo(self.grass16, (32, 32))
        self.grass48 = grassTest.scaleTileTo(self.grass16, (48, 48))
        self.grass64 = grassTest.scaleTileTo(self.grass16, (64, 64))
        self.grassA = grassTest.scaleTileTo(self.grass16, (64, 48))

        #self.viewport.vpChanged.add(Event(self.scaleAllSpriteSheet, 3))
    
    def scaleAssets(self, vsce : ViewportSettingsChangedEvent):
        pass

    def debug(self):
        self.viewport.visualDebug.display(f"Level Tile Scale: {Level.TILE_SCALE}", self.red)

    def loop(self):
        keep : bool = True
        while keep:
            self.clock.tick(self.targetFps)
            self.viewport.screen.fill(self.black)
            self.viewport.screen.blit(self.levelZero.lvlStatic, (0, 0))

            frameTime : float = self.clock.get_fps()
            frameRate : int = int(frameTime if frameTime > 0 else 0)

            #self.viewport.debug()
            #self.debug()
            #self.viewport.visualDebug.reset()

            self.levelZero.lvlStatic.blit(self.grass16, (0, 0))
            self.levelZero.lvlStatic.blit(self.grass32, (16, 0))
            self.levelZero.lvlStatic.blit(self.grass48, (48, 0))
            self.levelZero.lvlStatic.blit(self.grass64, (48 + 48, 0))
            self.levelZero.lvlStatic.blit(self.grassA, (48 + 48 + 64, 0))

            for event in pgEvent.get():
                if (event.type == pg.QUIT):
                    keep = False
                self.viewport.handleEvent(event)
                
            pgDisplay.flip()
        pg.quit()