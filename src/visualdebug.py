import pygame as pg
import pygame.font as pgFont
from viewportsettingschangedevent import *

class VisualDebug:
    def __init__(self, 
        startPos : list,
        windowHeigth : int,
        delta : int,
        fontSize : int,
        fontName : str):
        
        self.nextPos = startPos
        self.window : pg.Surface = None
        self.windowHeigth = windowHeigth

        self.delta = delta
        self.deltaScale = delta
        
        self.fontSize = fontSize
        self.fontScale = fontSize

        self.fontName : str = fontName
        self.font : pgFont.Font = pgFont.SysFont(fontName, self.fontScale)

    def display(self, txt : str, color : pg.Color):
        text = self.font.render(txt, True, color)
        self.window.blit(text, self.nextPos)
        self.nextPos[1] += self.deltaScale

    def reset(self):
        self.nextPos[1] = 0

    def onViewportChanged(self, vpce : ViewportSettingsChangedEvent):
        print(vpce.getRatioSize())
        #self.setWindowHeigth(vpce.viewport.size[1])
        pass

    def setWindow(self, window):
        self.window = window