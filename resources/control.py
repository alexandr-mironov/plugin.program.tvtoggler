import xbmc
import xbmcgui

# import resources.plugin  # noqa
xbmc.executebuiltin('CECToggleState')

button = xbmcgui.ControlButton(350, 500, 80, 30, "TV OFF")