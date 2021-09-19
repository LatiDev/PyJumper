import pygame as pg
import pygame.transform as pgTransf

def scaleSurface( 
    tile : pg.Surface, 
    scale : tuple, 
    transparent : tuple):
    
    scaleImage = pg.Surface(scale)
    pgTransf.scale(tile, scale, scaleImage)
    scaleImage.set_colorkey(transparent)
    
    return scaleImage