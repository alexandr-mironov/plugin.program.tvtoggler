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

    xbmcplugin.addDirectoryItems(handle, item_list, len(item_list))
    xbmcplugin.endOfDirectory(handle)
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_TITLE)
