import pygame as pg
from tile import *
from entity import *
from animationmanager import *

class Sprite(Tile, Entity):
    """
    Movable and Animable Tile
    """
    def __init__(self,
        position: tuple,
        animationMngr : AnimationManager, 
        type : list = [], 
        imageChangedListenners : list = [], 
        rgbCode : tuple = None):

        self.animationMngr = animationMngr        
        super().__init__(animationMngr.getCurrentFrame(), position, type, imageChangedListenners, rgbCode)

    def onUpdate(self, delta: float):
        super().onUpdate(delta)
        self.animationMngr.stepFrame()

    def play(self, index : int):
        self.animationMngr.setCurrentAnimation(index)
