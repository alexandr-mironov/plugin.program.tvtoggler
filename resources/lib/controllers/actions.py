import xbmc  # noqa


def on(router):
    xbmc.executebuiltin('CECActivateSource')
    router.redirect('root', 'index')


def off(router):
    if xbmc.Player().isPlaying():
        xbmc.executebuiltin("PlayerControl(Stop)")
    xbmc.executebuiltin('CECStandby')
    router.redirect('root', 'index')
