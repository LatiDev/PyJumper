import pygame as pg
import pygame.transform as pgTrans
from animation import *

class AnimationManager:
    """
    Handles the Play, Stop, Reset and Change of Animations
    """
    def __init__(self,
        animations : list[Animation],
        defaultAnimation : int) -> None:
        
        self.isFlip : bool = False

        self.animations = animations
        self.default : int = defaultAnimation
        self.curAnimation : Animation = self.getDefaultAnimation()
        self.curFrame : pg.Surface = self.curAnimation.step()

    def getDefaultAnimation(self) -> Animation:
        return self.animations[self.default]

    def getCurrentAnimation(self) -> Animation:
        """
        Returns the Current Animation
        """ 
        return self.curAnimation

    def getCurrentFrame(self) -> pg.Surface:
        """
        Returns the Current Animation Frame
        """ 
        return self.curFrame

    def setCurrentAnimation(self, index : int):
        """
        Set Current Animation to Play
        """
        next = self.animations[index]
        if (self.curAnimation != next):
            self.curAnimation = next
    
    def stepFrame(self):
        """
        Step the Current Animation (Should be Executed Every Frame)
        """
        nextStep = self.curAnimation.step()
        self.curFrame = self.curFrame
        if (self.isFlip):
            self.curFrame = pgTrans.flip(nextStep, True, False)
            