from viewportsettings import *

class ViewportSettingsChangedEvent:
    def __init__(self, 
        ogVp : ViewportSettings,
        vp : ViewportSettings) -> None:
        
        self.ogVp = ogVp
        self.viewport = vp

    def getRatioSize(self) -> tuple[float]:
        ratioWidth : float = self.viewport.size[0] / self.ogVp.size[0]
        ratioHeigth : float =  self.viewport.size[1] / self.ogVp.size[1]
        
        return (ratioWidth, ratioHeigth)