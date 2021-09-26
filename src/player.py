import math
import pygame as pg
import pygame.key as pg_key
import pygame.mouse as pg_mouse
import pygame.event as pg_event
import pygame.transform as tf
from character import *

class Player(Character):
    def __init__(self,
        position: tuple, 
        animationMngr: AnimationManager, 
        movementSpeed: int, 
        jumpSpeed: int, 
        maxJumps: int, 
        type: list, 
        rgbCode: tuple):
        super().__init__(position, animationMngr, movementSpeed, jumpSpeed, maxJumps, type, rgbCode) 

    def move(self, bodys):
        playerInput = getInput()
        super().move(playerInput, bodys)
