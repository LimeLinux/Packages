#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob

WorkDir="."

def install():
    pisitools.insinto("/usr/share/hunspell/tr-TR.aff", "tr.aff")
    pisitools.insinto("/usr/share/hunspell/tr-TR.dic", "tr.dic")
    #for other applications
    pisitools.dosym("/usr/share/hunspell/tr-TR.aff", "/usr/lib/libreoffice/share/extensions/hunspell_tr/dictionaries/tr-TR.aff")
    pisitools.dosym("/usr/share/hunspell/tr-TR.dic", "/usr/lib/libreoffice/share/extensions/hunspell_tr/dictionaries/tr-TR.dic")

    pisitools.dodoc("README")
