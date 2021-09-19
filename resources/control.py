import xbmc
import xbmcgui


class TVControl(xbmcgui.Window):
    def __init__(self):
        self.btnOff = xbmcgui.ControlButton(350, 500, 80, 30, "TV OFF")
        self.btnOn = xbmcgui.ControlButton(350, 500, 80, 30, "TV ON")

    def onControl(self, control):
        if control == self.btnOff:
            if xbmc.Player().isPlaying():
                xbmc.executebuiltin("PlayerControl(Stop)")
            xbmc.executebuiltin('CECStandby')
        if control == self.btnOn:
            xbmc.executebuiltin('CECActivateSource')
