import pygame as pg
import pygame.draw as pgDraw
import vectormath as vm

class Boundary():
    def __init__(self, 
        x1 : float, 
        y1 : float,
        x2 : float, 
        y2 : float,
        color : pg.Color = pg.Color(255, 255, 255)):

        self.start = vm.Vector2(x1, y1)
        self.end = vm.Vector2(x2, y2)
        self.color = color

    def draw(self, surface : pg.Surface):
        pgDraw.line(surface, self.color, self.start, self.end, 1)

    def __repr__(self) -> str:
        return f"Start: {self.start.x}, {self.start.y} | End: {self.end.x}, {self.end.y}"