#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools, shelltools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-i")
    shelltools.system("./bootstrap")
    autotools.configure("--disable-static \
                         --enable-relocatable \
                         --enable-aspell \
                         --enable-zemberek \
                         --enable-myspell \
                         --with-myspell-dir=/usr/share/hunspell \
                         --disable-ispell \
                         --disable-uspell \
                         --disable-hspell")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/lib/libenchant-2.so.2.2.3", "/usr/lib/libenchant.so.1")
    pisitools.dosym("/usr/lib/pkgconfig/enchant-2.pc", "/usr/lib/pkgconfig/enchant.pc")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "HACKING")
