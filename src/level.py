import pygame.math as pgMath
from assetmanager import *
from boundary import *
from spritesheet import *
from tile import *
from eventdivuser import *
from viewportsettingschangedevent import *

class Level:
    ALL = []
    COUNT = 3
    TILE_SCALE = (16, 16)
    def __init__(self, 
        image : PILImage.Image):

        self.pixels = image.load()
        self.imgSize = image.size

        self.playerPostition : tuple = None
        self.boundaries : list[Boundary] = []
        self.terrainTiles : list[Tile] = []
    
        #Level.TILE_SCALE[0] * self.imgSize[0], Level.TILE_SCALE[1] * self.imgSize[1]

        lvlRect = pg.Rect(0, 0, Level.TILE_SCALE[0] * self.imgSize[0], Level.TILE_SCALE[1] * self.imgSize[1])
        self.lvlStatic = pg.Surface(lvlRect.size)

    def create(self,
        screenSize : tuple,
        aroundDirt : bool = False):
        

        lastRgbCode : tuple = NONE_RGB
        lastSS : SpriteSheet = None
        
        horiBounds : list[Boundary] = []
        vertiBounds : list[Boundary] = []
        
        for y in range(self.imgSize[0]):
            for x in range(self.imgSize[1]):
                pixelCurrent = self.pixels[x, y]
                realPosition = (x * Level.TILE_SCALE[0], y * Level.TILE_SCALE[1])

                if pixelCurrent != lastRgbCode:
                    for spritesheet in SpriteSheet.ALL:
                        if (spritesheet.color == pixelCurrent):
                            lastSS = spritesheet
                            lastRgbCode = spritesheet.color
                            break;
                    if (pixelCurrent != lastRgbCode):
                        lastSS = None
                        lastRgbCode = pixelCurrent

                if (lastSS != None):
                    if (lastSS.proccess == PROCESS_TERRAIN):                        
                        isYMin = y == 0
                        isXMin = x == 0
                        isYMax = y == self.imgSize[1] - 1
                        isXMax = x == self.imgSize[0] - 1

                        canUp = y > 0
                        canRigth = x < self.imgSize[0] - 1
                        canDown = y < self.imgSize[1] - 1
                        canLeft = x > 0

                        canUpLeft = canUp and canLeft
                        canUpRigth = canUp and canRigth
                        canDownLeft = canDown and canLeft
                        canDownRigth = canDown and canRigth

                        isUpType = canUp and self.pixels[x, y - 1] == lastSS.color
                        isLeftType = canLeft and self.pixels[x - 1, y] == lastSS.color
                        isDownType = canDown and self.pixels[x, y + 1] == lastSS.color
                        isRigthType = canRigth and self.pixels[x + 1, y] == lastSS.color

                        isUpDirt = canUp and self.pixels[x, y - 1] == DIRT_RGB
                        if (aroundDirt and isYMin): 
                            isUpDirt = True
                        
                        isDownDirt = canDown and self.pixels[x, y + 1] == DIRT_RGB
                        if (aroundDirt and isYMax): 
                            isDownDirt = True
                        
                        isLeftDirt = canLeft and self.pixels[x - 1, y] == DIRT_RGB
                        if (aroundDirt and isXMin): 
                            isLeftDirt = True
                        
                        isRigthDirt = canRigth and self.pixels[x + 1, y] == DIRT_RGB 
                        if (aroundDirt and isXMax): 
                            isRigthDirt = True

                        isUpLeftDirt = canUpLeft and self.pixels[x - 1, y - 1] == DIRT_RGB
                        if (aroundDirt and isXMin and isYMin): 
                            isUpLeftDirt = True
                        
                        isUpRigthDirt = canUpRigth and self.pixels[x + 1, y - 1] == DIRT_RGB
                        if (aroundDirt and isXMax and isYMin): 
                            isUpRigthDirt = True
                        
                        isDownRigthDirt = canDownRigth and self.pixels[x + 1, y + 1] == DIRT_RGB
                        if (aroundDirt and isXMax and isYMax): 
                            isDownRigthDirt = True
                        
                        isDownLeftDirt = canDownLeft and self.pixels[x - 1, y + 1] == DIRT_RGB
                        if (aroundDirt and isXMin and isYMax): 
                            isDownLeftDirt = True

                        nextTileRect : pg.Rect = pg.Rect(realPosition, self.imgSize)

                        toVect = lambda p : pgMath.Vector2(p[0], p[1])
                        toBound = lambda s, e : Boundary(s.x, s.y, e.x, e.y)

                        vertiBound : Boundary = None
                        horiBound : Boundary = None
                        indexTileToAdd : tuple = NONE_RGB

                        if isDownType and isRigthType:
                            if (isDownRigthDirt):
                                indexTileToAdd = SS_TILE_UP_LEFT
                                vertiBound = toBound(toVect(nextTileRect.topleft), toVect(nextTileRect.bottomleft))
                                horiBound = toBound(toVect(nextTileRect.topleft), toVect(nextTileRect.topright))
                            elif (isUpLeftDirt):
                                indexTileToAdd = SS_TILE_UP_LEFT_ALT

                        elif isUpType and isRigthType:
                            if (isUpRigthDirt):
                                indexTileToAdd = SS_TILE_DOWN_LEFT
                                vertiBound = toBound(toVect(nextTileRect.topleft), toVect(nextTileRect.bottomleft))
                                horiBound = toBound(toVect(nextTileRect.bottomleft), toVect(nextTileRect.bottomright))
                            elif (isDownLeftDirt):
                                indexTileToAdd = SS_TILE_DOWN_LEFT_ALT

                        elif isDownType and isLeftType:
                            if (isDownLeftDirt):
                                indexTileToAdd = SS_TILE_UP_RIGTH
                                vertiBound = toBound(toVect(nextTileRect.topright), toVect(nextTileRect.bottomright))
                                horiBound = toBound(toVect(nextTileRect.topleft), toVect(nextTileRect.topright))
                            elif (isUpRigthDirt):
                                indexTileToAdd = SS_TILE_UP_RIGTH_ALT

                        elif isUpType and isLeftType:                        
                            if (isUpLeftDirt):
                                indexTileToAdd = SS_TILE_DOWN_RIGTH
                                vertiBound = toBound(toVect(nextTileRect.topright), toVect(nextTileRect.bottomright))
                                horiBound = toBound(toVect(nextTileRect.bottomleft), toVect(nextTileRect.bottomright))
                            elif (isDownRigthDirt):
                                indexTileToAdd = SS_TILE_DOWN_RIGTH_ALT

                        elif not isUpType and not isDownType:
                            if (isUpDirt):
                                indexTileToAdd = SS_TILE_DOWN
                                horiBound = toBound(toVect(nextTileRect.bottomleft), toVect(nextTileRect.bottomright))
                            elif (isDownDirt):
                                indexTileToAdd = SS_TILE_UP
                                horiBound = toBound(toVect(nextTileRect.topleft), toVect(nextTileRect.topright))
                        
                        elif not isLeftType and not isRigthType:
                            if (isLeftDirt):
                                indexTileToAdd = SS_TILE_RIGTH
                                vertiBound = toBound(toVect(nextTileRect.topright), toVect(nextTileRect.bottomright))

                            elif (isRigthDirt):
                                indexTileToAdd = SS_TILE_LEFT
                                vertiBound = toBound(toVect(nextTileRect.topleft), toVect(nextTileRect.bottomleft))

                        if vertiBound:
                            indexVerti : int = -1
                            for i in range(len(vertiBounds)):
                                verti = vertiBounds[i]
                                if (verti.start.x == vertiBound.start.x and verti.end.x == vertiBound.end.x and
                                verti.end.y + Level.TILE_SCALE[1] == vertiBound.end.y):
                                    indexVerti = i
                        
                            if (indexVerti == -1):
                                vertiBounds.append(vertiBound)
                            else:
                                verti = vertiBounds[indexVerti]
                                verti.end = vertiBound.end
                        
                        if horiBound:
                            indexHori : int = -1
                            for i in range(len(horiBounds)):
                                hori = horiBounds[i]
                                if (hori.start.y == horiBound.start.y and hori.end.y == horiBound.end.y and
                                hori.end.x + Level.TILE_SCALE[0] == horiBound.end.x):
                                    indexHori = i
                                
                            if (indexHori == -1):
                                horiBounds.append(horiBound)
                            else:
                                hori = horiBounds[i]
                                hori.end = horiBound.end

                        nextTileSpriteID : pg.Surface = lastSS.tiles[indexTileToAdd[2]]
                        #print(nextTileRect)
                        self.terrainTiles.append(Tile(pixelCurrent, realPosition))
                        self.lvlStatic.blit(nextTileSpriteID, realPosition)

                    elif (lastSS.proccess == PROCESS_ACTOR):
                        if (pixelCurrent == PLAYER_RGB):
                            self.playerPostition = realPosition
        
        self.boundaries.extend(horiBounds)
        self.boundaries.extend(vertiBounds)

        self.boundaries.append(Boundary(0, 0, screenSize[0], 0))
        self.boundaries.append(Boundary(screenSize[0], 0, screenSize[0], screenSize[1]))
        self.boundaries.append(Boundary(screenSize[0], screenSize[1], 0, screenSize[1]))
        self.boundaries.append(Boundary(0, screenSize[1], 0, 0))

    def setlvlImg(self, screenSize :tuple, tileScale : tuple):
        #self.lvlRect = pg.Rect(0, 0, self.imgSize[0] * tileScale[0], self.imgSize[1] * tileScale[1])
        #self.lvlStatic = pg.Surface(self.lvlRect.size)
        
        #self.create(screenSize, False, False)
        pass