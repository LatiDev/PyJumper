from spritesheet import *

class SpriteSheetTerrain(SpriteSheet):
    def __init__(self, 
        sheet: pg.Surface, 
        tileSize: tuple,
        proccess: int, 
        color: tuple,
        scaleTo : int = 1,
        tranparent: tuple = (0, 0, 0, 255)):
        super().__init__(sheet, tileSize, proccess, color, scaleTo, tranparent)

        self.addTileAt(SS_TILE_UP_LEFT) #0
        self.addTileAt(SS_TILE_UP)
        self.addTileAt(SS_TILE_UP_RIGTH)
        self.addTileAt(SS_TILE_LEFT)
        self.addTileAt(SS_TILE_CENTER)
        self.addTileAt(SS_TILE_RIGTH)
        self.addTileAt(SS_TILE_DOWN_LEFT)
        self.addTileAt(SS_TILE_DOWN)
        self.addTileAt(SS_TILE_DOWN_RIGTH)
        self.addTileAt(SS_TILE_UP_LEFT_ALT)
        self.addTileAt(SS_TILE_UP_RIGTH_ALT)
        self.addTileAt(SS_TILE_DOWN_LEFT_ALT)
        self.addTileAt(SS_TILE_DOWN_RIGTH_ALT) #12
    
    def load(
        filename: str, 
        tileSize: tuple, 
        proccess: int, 
        color: tuple,
        scaleTo : int = 1,
        tranparent: tuple = (0, 0, 0, 255)):
        
        img = loadAsset(SPRITESHEET_PATH, filename)
        return SpriteSheetTerrain(img, tileSize, proccess, color, scaleTo, tranparent)