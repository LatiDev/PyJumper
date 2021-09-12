import pygame as pg
import pygame.font as pgFont
from viewportsettings import *

class VisualDebug:
    def __init__(self, 
        startPos : list,
        windowHeigth : int,
        delta : int,
        fontProportion : int,
        fontName : str):
        
        self.nextPos = startPos
        self.window : pg.Surface = None
        self.windowHeigth = windowHeigth

        self.delta = delta
        self.proportion = fontProportion

        self.fontName : str = fontName
        self.font : pgFont.Font = pgFont.SysFont(fontName, int(windowHeigth / fontProportion))

    def display(self, txt : str, color : pg.Color):
        text = self.font.render(txt, True, color)
        self.window.blit(text, self.nextPos)
        self.nextPos[1] += int(self.windowHeigth / self.delta)

    def reset(self):
        self.nextPos[1] = 0

    def onViewportChanged(self, vp : ViewportSettings):
        self.setWindowHeigth(vp.size[1])

    def setWindowHeigth(self, wh : int):
        self.windowHeigth = wh
        self.font = pgFont.SysFont(self.fontName, int(wh / self.proportion))

    def setWindow(self, window):
        self.window = window

    def getFontSize(self) -> int:
        return int(self.windowHeigth / self.proportion)
    
    def getDelta(self) -> int:
        return int(self.windowHeigth / self.delta)