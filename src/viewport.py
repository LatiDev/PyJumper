import os
import pygame as pg
import pygame.image as pgImage
import pygame.transform as pgTransf
import pygame.time as pgTime
import pygame.mouse as pgMouse
import pygame.event as pgEvent
import pygame.display as pgDisplay
from viewportsettings import *
from visualdebug import *
from eventdivuser import *

class Viewport:
    def __init__(self, width, heigth, debugColor = pg.Color(255, 255, 255), targetFps = 60):
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        self.clock = pgTime.Clock()
        self.monitorData = pgDisplay.Info()
        self.targetFps : int = targetFps

        self.debugColor = debugColor

        self.isFullScreen : bool = False
        self.isMaximized : bool = False

        self.vpChanged : EventDivuser = EventDivuser(lambda e : e.order)

        self.vpSettings = ViewportSettings((width, heigth), 0, 1)
        self.vpFsSettings =  ViewportSettings((self.monitorData.current_w, self.monitorData.current_h), pg.HWSURFACE | pg.DOUBLEBUF, 1)
        self.curVpSettings = self.vpSettings

        self.visualDebug : VisualDebug = VisualDebug([5, 5], self.vpSettings.size[1], 10, 10, "Verdana")
        self.vpChanged.add(Event(self.visualDebug.onViewportChanged, 1))

        self.screen : pg.Surface = None
        self.setViewportSettings(self.vpSettings)
        
        self.visualDebug.setWindow(self.screen)

        if self.isFullScreen:
            self.setViewportSettings(self.vpFsSettings)
            pgDisplay.toggle_fullscreen()

    def setViewportSettings(self, vp : ViewportSettings):
        vsce = ViewportSettingsChangedEvent(self.curVpSettings, vp) 
        
        self.curVpSettings = vp
        self.vpChanged.diffuse(vsce)
        self.screen = pgDisplay.set_mode(vp.size, vp.flags, vsync=vp.vsync)

    def debug(self):
        self.visualDebug.display(f"Monitor Size: {(self.monitorData.current_w, self.monitorData.current_h)}", self.debugColor)
        self.visualDebug.display(f"Window Size: {self.curVpSettings.size}", self.debugColor)
        self.visualDebug.display(f"Flags: {self.curVpSettings.flags}", self.debugColor)
        self.visualDebug.display(f"Vsync: {self.curVpSettings.vsync}", self.debugColor)
        self.visualDebug.display(f"Font size: {self.visualDebug.fontScale}", self.debugColor)
        self.visualDebug.display(f"Delta: {self.visualDebug.deltaScale}", self.debugColor)
        self.visualDebug.display(f"Is Fullscreen: {self.isFullScreen}", self.debugColor)

    def handleEvent(self, event : pgEvent.Event):
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_f):
                self.isFullScreen = not self.isFullScreen
                if (self.isFullScreen):
                    if (self.isMaximized):
                        self.isFullScreen = not self.isFullScreen
                    else:
                        self.setViewportSettings(self.vpFsSettings)
                        pgDisplay.toggle_fullscreen()
                else:
                    pgDisplay.toggle_fullscreen()
                    self.setViewportSettings(self.vpSettings)
            elif (event.key == pg.K_a):
                self.setViewportSettings(self.vpSettings)
            elif (event.key == pg.K_z):
                self.setViewportSettings(ViewportSettings((1600, 900), 0, 1))
            elif (event.key == pg.K_e):
                self.setViewportSettings(self.vpFsSettings)
        elif event.type == pg.WINDOWEVENT:
            if event.event == pg.WINDOWEVENT_MAXIMIZED:
                self.isMaximized = True 
            elif event.event == pg.WINDOWEVENT_MINIMIZED or event.event == pg.WINDOWEVENT_RESTORED:
                self.isMaximized = False