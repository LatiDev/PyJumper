import pygame as pg

class Tile:
    def __init__(self, 
        color : pg.Color,
        position : tuple):
        
        self.color = color
        self.position = position