import pygame
import time
import typing

NO_RESET = 0
AUTO_RESET = 1

class Animation:
    def __init__(
        self, 
        list : typing.List[pygame.Surface], 
        stepFrame : float,
        autoReset : bool = False):
        
        self.image = list
        self.stepFrame = stepFrame

        self.doesReset : int = autoReset
        self.nowTime : float = time.time()
        self.indexAnimation : int = 0
        self.nbAnimations : int = len(list) - 1
    
    def step(self) -> pygame.Surface:
        animation = self.image[self.indexAnimation]
        if (self.wait()):
            if (self.indexAnimation < self.nbAnimations):
                self.indexAnimation += 1
            elif (self.doesReset == AUTO_RESET):
                self.indexAnimation = 0

        return animation
    
    def wait(self) -> bool:
        timeElasped : bool = time.time() - self.nowTime > self.stepFrame
        if timeElasped:
            self.nowTime = time.time()
        return timeElasped

    def __repr__(self) -> str:
        return f"{self.indexAnimation}"