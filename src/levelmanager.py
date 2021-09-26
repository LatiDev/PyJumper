import copy
from level import *
from utils import *
from assetmanager import *
from viewportsettingschangedevent import *

class LevelManager:
    def __init__(self, screenSize : tuple):
        self.levels = loadAll(screenSize, 16, False)
        self.lvlIndex = 0
        self.transparent = (0, 0, 0, 255)
        self.scaledSize : tuple = (screenSize[1], screenSize[1])
        
        self.curlvl = None
        self.curlvlScaled = None

        self.updateCurrentLevel()
        
    def onViewportChanged(self, vsce : ViewportSettingsChangedEvent):
        heigth = vsce.viewport.size[1]
        self.scaledSize = (heigth, heigth)

        self.curlvlScaled.level = scaleSurface(self.curlvl.level, self.scaledSize, self.transparent)

    def updateCurrentLevel(self):
        self.curlvl = self.levels[self.lvlIndex]
        self.curlvlScaled = copy.copy(self.curlvl)        

    def gotToLevel(self, delta: int):
        self.lvlIndex += delta
        if (self.lvlIndex > Level.COUNT - 1):
            self.lvlIndex = Level.COUNT - 1
        elif (self.lvlIndex < 0):
            self.lvlIndex = 0

        self.updateCurrentLevel()
        self.curlvlScaled.level = scaleSurface(self.curlvl.level, self.scaledSize, self.transparent)