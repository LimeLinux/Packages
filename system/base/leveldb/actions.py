#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.chmod("build_detect_platform", 0755)
    autotools.make("-j2")


def install():
    pisitools.dolib_so("out-shared/libleveldb.so.1.20")
    pisitools.insinto("/usr/lib/", "out-shared/libleveldb.so.1")
    pisitools.insinto("/usr/lib/", "out-shared/libleveldb.so")

    pisitools.insinto("/usr/include", "include/*")
    pisitools.insinto("/usr/include/leveldb", "helpers/memenv/memenv.h")

    pisitools.dodoc("README.md", "LICENSE", "NEWS", "AUTHORS", "TODO")
