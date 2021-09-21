import xbmc  # noqa
import xbmcgui

ACTION_PREVIOUS_MENU = 10  # ESC
ACTION_NAV_BACK = 92  # Backspace


class TVControl(xbmcgui.Window):
    def __init__(self):
        self.btnOff = xbmcgui.ControlButton(350, 400, 180, 80, "TV OFF")
        self.addControl(self.btnOff)
        self.btnOn = xbmcgui.ControlButton(350, 500, 180, 80, "TV ON")
        self.addControl(self.btnOn)
        self.setFocus(self.btnOff)

    def onAction(self, action):  # noqa
        if action == ACTION_NAV_BACK or action == ACTION_PREVIOUS_MENU:
            self.close()

    def onControl(self, control):  # noqa
        if control == self.btnOff:
            if xbmc.Player().isPlaying():
                xbmc.executebuiltin("PlayerControl(Stop)")
            xbmc.executebuiltin('CECStandby')
        if control == self.btnOn:
            xbmc.executebuiltin('CECActivateSource')
