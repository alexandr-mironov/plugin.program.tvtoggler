import xbmc # noqa
import xbmcgui


class TVControl(xbmcgui.Window):
    def __init__(self):
        self.btnOff = xbmcgui.ControlButton(350, 400, 180, 80, "TV OFF")
        self.btnOn = xbmcgui.ControlButton(350, 500, 180, 80, "TV ON")
        self.setFocus(self.btnOff)

    def onControl(self, control): # noqa
        if control == self.btnOff:
            if xbmc.Player().isPlaying():
                xbmc.executebuiltin("PlayerControl(Stop)")
            xbmc.executebuiltin('CECStandby')
        if control == self.btnOn:
            xbmc.executebuiltin('CECActivateSource')
