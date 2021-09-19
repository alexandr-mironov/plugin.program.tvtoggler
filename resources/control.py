import xbmc
import xbmcgui


class TVControl(xbmcgui.Window):
    def __init__(self):
        self.btnOff = xbmcgui.ControlButton(350, 500, 80, 30, "TV OFF")

    def onControl(self, control):
        if control == self.btnOff:
            xbmc.executebuiltin('CECToggleState')
        if control == self.button1:
            self.message('you pushed the 2nd button')
        if control == self.button2:
            self.message('you pushed the 3rd button')
