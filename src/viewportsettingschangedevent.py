from viewportsettings import *

class ViewportSettingsChangedEvent:
    def __init__(self, 
        lastVp : ViewportSettings,
        vp : ViewportSettings) -> None:
        
        self.lastVp = lastVp
        self.viewport = vp

    def getRatioSize(self) -> tuple[float]:
        ratioWidth : float = self.viewport.size[0] / self.lastVp.size[0]
        ratioHeigth : float =  self.viewport.size[1] / self.lastVp.size[1]
        
        return (ratioWidth, ratioHeigth)