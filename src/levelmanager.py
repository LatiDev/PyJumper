import copy
from pygame import Surface
from level import *
from utils import *
from exittype import *
from assetmanager import *
from viewportsettingschangedevent import *


# Charge les niveaux, switcher entre les niveaux
# upscale level
class LevelManager:
    def __init__(self, llo : LevelCreateOption):
        self.__levelLoadOption = llo
        
        self.__currentLevel : Level = None
        self.__currentLevelIndex : int = llo.id
        self.__currentLevelSurface : Surface = None
        self.setLevel(llo.id)

        self.__transparent = (0, 0, 0, 255)
        self.__scaledSize : tuple = (llo.screenSize[1], llo.screenSize[1])

        self.__updateLevelSurface()
        
    def onViewportChanged(self, vsce : ViewportSettingsChangedEvent):
        heigth = vsce.viewport.size[1]
        self.__scaledSize = (heigth, heigth)

        self.__updateLevelSurface()      
    
    def __updateLevelSurface(self):
        self.__currentLevelSurface = scaleSurface(
            self.__currentLevel.level, 
            self.__scaledSize, 
            self.__transparent)

    def getLevelSurface(self) -> Surface:
        return self.currentLevelSurface

    def setIndex(self, index) -> int:
        if (index > 0 and index < Level.COUNT):
            self.__currentLevelIndex = index
        else:
            return EXIT_ERROR
        return EXIT_SUCCESS

    def setLevel(self, index):
        if not self.setIndex(index):
            self.__currentLevel = createLevel(self.__levelLoadOption)
            self.__updateLevelSurface()

    def setLevelLoadOption(self, llo : LevelCreateOption):
        self.__levelLoadOption = llo
        self.setLevel(llo.id)