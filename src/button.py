import pygame as pg
import pygame.mouse as pgMouse
import pygame.event as pgEvent
from animation import *
from animationmanager import *

class Button:
    def __init__(self,
        idleAnimation : Animation,
        hoverAnimation : Animation,
        clickAnimation : Animation):

        self.cursorInLastFrame : bool = False
        self.aniMngr = AnimationManager([idleAnimation, hoverAnimation, clickAnimation], idleAnimation)
    
    def onUpdate(self):
        mousePos = pgMouse.get_pos()
        curFrame = self.aniMngr.getCurrentFrame()
        curFrameRect = curFrame.get_rect()

        cursorInCurFrame = curFrameRect.collidepoint(mousePos)
        print(cursorInCurFrame)


        self.cursorInLastFrame = cursorInCurFrame