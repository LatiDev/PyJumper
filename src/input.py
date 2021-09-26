import pygame as pg
import pygame.key as pg_key

NONE = 0 
LEFT = 1 
DOWN = 2 
RIGTH = 4 
UP = 8

def getInput() -> int:
    key = pg_key.get_pressed()
    direction : int = NONE

    if key[pg.K_UP]:
        direction += UP
    if key[pg.K_RIGHT]:
        direction += RIGTH
    if key[pg.K_DOWN]:
        direction += DOWN
    if key[pg.K_LEFT]:
        direction += LEFT

    return direction