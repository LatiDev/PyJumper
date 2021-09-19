import pygame as pg
import pygame.font as pgFont
from viewportsettingschangedevent import *

class VisualDebug:
    def __init__(self, 
        startPos : list,
        delta : int,
        fontSize : int,
        fontName : str):
        
        self.nextPos = startPos
        self.window : pg.Surface = None

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

    def space(self):
        self.nextPos[1] += self.deltaScale

    def onViewportChanged(self, vpce : ViewportSettingsChangedEvent):
        ratio = vpce.getRatioSize()
        self.deltaScale = int(self.delta * ratio[1])
        self.fontScale = int(self.fontSize * ratio[1])
        self.font : pgFont.Font = pgFont.SysFont(self.fontName, self.fontScale)

    def setWindow(self, window):
        self.window = window