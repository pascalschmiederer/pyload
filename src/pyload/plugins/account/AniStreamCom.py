# -*- coding: utf-8 -*-

from pyload.plugins.internal.xfsaccount import XFSAccount


class AniStreamCom(XFSAccount):
    __name__ = "AniStreamCom"
    __type__ = "account"
    __version__ = "0.05"
    __status__ = "testing"

    __pyload_version__ = "0.5"

    __description__ = """Ani-Stream.com account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("Walter Purcaro", "vuolter@gmail.com")]

    PLUGIN_DOMAIN = "ani-stream.com"