from future import standard_library
standard_library.install_aliases()  # noqa: E402
import xbmcplugin
import xbmcgui


def index(router, _params=None):
    handle = router.session.handle

    item_list = [
        (router.actions_url('on'), xbmcgui.ListItem(label='ON'), False),
        (router.actions_url('off'), xbmcgui.ListItem(label='OFF'), False)
    ]

    # li = xbmcgui.ListItem(label=mov['title'], label2=mov['description'])
    # li.setArt({'poster': api.art_url(mov['poster_id'])})
    # if mov['fanart_id']:
    #     li.setArt({'fanart': api.art_url(mov['fanart_id'], 630, 354)})
    # li.setInfo('video', dict(
    #     title=mov['title'],
    #     plot=mov['description']
    # ))
    # # li.setProperty('IsPlayable', 'true')
    # url = router.root_url('play', id=mov['id'], hls_id=mov['hls_id'])
    # item_list.append((url, li, False))

    xbmcplugin.addDirectoryItems(handle, item_list, len(item_list))
    xbmcplugin.endOfDirectory(handle)
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_TITLE)
