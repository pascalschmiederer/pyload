# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadcrypter import DeadCrypter


class WuploadComFolder(DeadCrypter):
    __name__ = "WuploadComFolder"
    __type__ = "crypter"
    __version__ = "0.07"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"http://(?:www\.)?wupload\.com/folder/\w+"
    __config__ = [("activated", "bool", "Activated", True)]

    __description__ = """Wupload.com folder decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]