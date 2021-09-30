from future import standard_library
standard_library.install_aliases()  # noqa: E402

import sys
import xbmcplugin
from resources.lib.router import Router
from resources.lib.controllers import (
    root,
    actions
)

router = Router('plugin://plugin.program.tvtoggler')
router.add('/', root, 'index')
router.add('/off', actions, 'off')
router.add('/on', actions, 'on')

if len(sys.argv) == 4:
    xbmcplugin.setContent(int(sys.argv[1]), 'videos')
    router.run(*sys.argv)

