import pygame as pg
import typing as tp
import pygame.transform as pgTransf
from viewportsettingschangedevent import *

class Tile:
    """
    Movable Image
    """
    def __init__(self, 
        image : pg.Surface, 
        position : tuple, 
        type : list = [], 
        imageChangedListenners : list = [], 
        rgbCode : tuple = None):       
        
        self.ogImage = image
        self.ogRect = image.get_rect()
        self.ogPos = position

        self.currentImage = None
        self.rect = None
        self.imageChangedListenners = imageChangedListenners        
        self.type = type
        self.rgbCode = rgbCode

        self.setImage(image, position)
    
    def onViewportChanged(self, vsce : ViewportSettingsChangedEvent):
        ratio = vsce.getRatioSize()
        ratioInt = (int(self.ogRect.width * ratio[1]), int(self.ogRect.height * ratio[1]))
        self.currentImage = self.scaleTileTo(self.ogImage, ratioInt)

        posRatio = (int(self.ogPos[0] * ratio[0]), int(self.ogPos[1] * ratio[1]))
        print(ratio)
        print(posRatio)
        self.setPosition(posRatio)

    def setImage(self, 
        image : pg.Surface, 
        position : tuple = None):
        """
        Set or Update the Image of the Tile
        """
        if image is not None:
            size = image.get_size()
            if position is None:
                # update image
                if (self.rect is not None and self.rect.width == size[0] and self.rect.height == size[1]):
                    self.currentImage = image
            else:
                # set image and rect
                self.currentImage = image
                self.rect : pg.Rect = pg.Rect(position[0], position[1], size[0], size[1])
            # notify all listenners
            for listenner in self.imageChangedListenners:
                listenner(image)
        else:
            raise Exception(f"image cant be None")
            #print(f"image cant be None")
    
    def scaleTileTo(self, tile : pg.Surface, scale : tuple, tranparent = (0, 0, 0, 255)):
        scaleImage = pg.Surface(scale)
        pgTransf.scale(tile, scale, scaleImage)
        scaleImage.set_colorkey(tranparent)
        
        return scaleImage

    def setPosition(self, 
        position : tuple):
        """
        Set Position of the Tile
        """
        self.rect.x = position[0]
        self.rect.y = position[1]

    def getPosition(self) -> tuple:
        """
        get Position of the Tile
        """        
        return (self.rect.x, self.rect.y)

    def AddPosition(self,
        delta : tuple) -> tuple:
        """
        Add Position to the Possition of the Tile
        """
        self.rect.x += delta[0]
        self.rect.y += delta[1]

    def setScale(self, 
        scale : tuple):
        """
        Set the Rectangle Scale of the Tile
        """
        self.rect.width = scale.x
        self.rect.height = scale.y

    def getScale(self) -> tuple:
        """
        Returns the Rectangle Scale of the Tile
        """
        return (self.rect.width , self.rect.height)
