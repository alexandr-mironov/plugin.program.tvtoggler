

def index(router):
    handle = router.session.handle

    item_list = []

    li = xbmcgui.ListItem(label=mov['title'], label2=mov['description'])
    li.setArt({'poster': api.art_url(mov['poster_id'])})
    if mov['fanart_id']:
        li.setArt({'fanart': api.art_url(mov['fanart_id'], 630, 354)})
    li.setInfo('video', dict(
        title=mov['title'],
        plot=mov['description']
    ))
    li.setProperty('IsPlayable', 'true')
    url = router.root_url('play', id=mov['id'], hls_id=mov['hls_id'])
    item_list.append((url, li, False))

    xbmcplugin.addDirectoryItems(handle, movies, len(movies))
    xbmcplugin.endOfDirectory(handle)
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_TITLE)