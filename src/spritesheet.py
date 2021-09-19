import pygame as pg
import pygame.image as pgImage
import pygame.transform as pgTransf
from viewportsettingschangedevent import *
from assetmanager import *

SS_TILE_UP_LEFT =           (0, 0, 0)
SS_TILE_UP =                (1, 0, 1)
SS_TILE_UP_RIGTH =          (2, 0, 2)
SS_TILE_LEFT =              (0, 1, 3)
SS_TILE_CENTER =            (1, 1, 4)
SS_TILE_RIGTH =             (2, 1, 5)
SS_TILE_DOWN_LEFT =         (0, 2, 6)
SS_TILE_DOWN =              (1, 2, 7)
SS_TILE_DOWN_RIGTH =        (2, 2, 8)
SS_TILE_UP_LEFT_ALT =       (3, 0, 9)
SS_TILE_UP_RIGTH_ALT =      (4, 0, 10)
SS_TILE_DOWN_LEFT_ALT =     (3, 1, 11)
SS_TILE_DOWN_RIGTH_ALT =    (4, 1, 12)

PROCESS_TERRAIN = 0
PROCESS_ACTOR = 1

NONE_RGB =          (0, 0, 0)
GRASS_RGB =         (0, 255, 0)
BRICK_RGB =         (0, 255, 128)
PIKE_RGB =          (255, 128, 0)
DIRT_RGB =          (255, 0, 0)
BACKGROUND_RGB =    (0, 0, 255)
PLAYER_RGB =        (255, 0, 255)

class SpriteSheet:
    ALL = []
    def __init__(self, 
        sheet : pg.Surface,
        tileSize : tuple,
        proccess : int,
        color : tuple,
        tranparent : tuple = (0, 0, 0, 255)):
        
        self.sheet = sheet
        self.tileSize = tileSize
        self.proccess = proccess
        self.color = color
        self.tranparent = tranparent

        self.tiles : list[pg.Surface] = []

        SpriteSheet.ALL.append(self)

    def getTileAt(self, position : tuple) -> pg.Surface:
        rect = pg.Rect(position[0] * self.tileSize[0], position[1] * self.tileSize[1], self.tileSize[0], self.tileSize[1])
        image = pg.Surface(rect.size)
        image.set_colorkey(self.tranparent)
        image.blit(self.sheet, (0, 0), rect)

        return image

    def addTileAt(self, position : tuple):
        tile = self.getTileAt(position)
        self.tiles.append(tile)

    def scaleTileTo(self, tile : pg.Surface, scale : tuple):
        scaleImage = pg.Surface(scale)
        pgTransf.scale(tile, scale, scaleImage)
        scaleImage.set_colorkey(self.tranparent)
        
        return scaleImage

    def scaleAllTileTo(self, scale : tuple):        
        for i in range(len(self.tiles)):
            self.tiles[i] = self.scaleTileTo(self.tiles[i], scale)

    def load(
        filename : str,
        tileSize : tuple,
        proccess : int,
        color : tuple,
        tranparent : tuple = (0, 0, 0, 255)):
        
        img = loadAsset(SPRITESHEET_PATH, filename)
        return SpriteSheet(img, tileSize, proccess, color, tranparent)
