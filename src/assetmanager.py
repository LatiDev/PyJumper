import os
import json
import pygame as pg
import pygame.image as pgImage
from PIL import Image as PILImage

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

def loadAsset(directory : str, file : str):
    path = f"{directory}/{file}"

    if (directory == SAVE_PATH):
        return loadSave()
    elif (directory == LEVEL_PATH):
        return PILImage.open(path)
    else:
        return pgImage.load(path)

def loadSave() -> dict:
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    
    if not os.path.exists(SAVE_PATH):
        createFile = open(SAVE_PATH, 'w+')
        createFile.close()

    isEmpty : bool = False
    with open(SAVE_PATH, 'r') as saveFile:
        firstLine = saveFile.readline()
        if not firstLine:
            isEmpty = True

    if (isEmpty):
        with open(SAVE_PATH, 'w') as saveFile:
            saveFile.write(json.dumps(DEFAULT_SAVE))

    saveData = open(SAVE_PATH, 'r')
    data = json.loads(saveData.readline())
    saveData.close()

    return data