import xbmc  # noqa


def on():
    xbmc.executebuiltin('CECActivateSource')


def off():
    if xbmc.Player().isPlaying():
        xbmc.executebuiltin("PlayerControl(Stop)")
    xbmc.executebuiltin('CECStandby')
