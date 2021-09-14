import os
import json
import pygame as pg
import pygame.image as pgImage
from spritesheet import *
from PIL import Image as PILImage

class AssetManager:
    ASSET_PATH =        f"assets"
    SAVE_PATH =         f"save/save.json"
    LEVEL_PATH =        f"{ASSET_PATH}/levels"
    SPRITESHEET_PATH =  f"{ASSET_PATH}/spritesheet"
    TILES_PATH =        f"{ASSET_PATH}/tiles"
    DEFAULT_SAVE = {
        "LAST_LEVEL_ID": 0,
        "LAST_SPAWNPOINT_ID": 0,
        "MUSICS_VOLUME": 0,
        "SOUNDS_VOLUME": 0,
        "TOTAL_DEATHS": 0
    }
    def __init__(self) -> None:
        pass

    def loadAsset(self, directory : str, file : str):
        path = f"{directory}/{file}"

        if (directory == AssetManager.SAVE_PATH):
            return self.loadSave()
        elif (directory == AssetManager.LEVEL_PATH):
            return PILImage.open(path)
        else:
            return pgImage.load(path)
    
    def loadSave(self) -> dict:
        if not os.path.exists(AssetManager.SAVE_PATH):
            os.mkdir(AssetManager.SAVE_PATH)
        
        if not os.path.exists(AssetManager.SAVE_PATH):
            createFile = open(AssetManager.SAVE_PATH, 'w+')
            createFile.close()

        isEmpty : bool = False
        with open(AssetManager.SAVE_PATH, 'r') as saveFile:
            firstLine = saveFile.readline()
            if not firstLine:
                isEmpty = True

        if (isEmpty):
            with open(AssetManager.SAVE_PATH, 'w') as saveFile:
                saveFile.write(json.dumps(AssetManager.DEFAULT_SAVE))

        saveData = open(AssetManager.SAVE_PATH, 'r')
        data = json.loads(saveData.readline())
        saveData.close()

        return data