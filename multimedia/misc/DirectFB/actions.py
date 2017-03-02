#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure(' --prefix=/usr --sysconfdir=/etc --enable-static \
                            --disable-silent-rules --enable-zlib --enable-x11 \
                            --enable-sdl --disable-vnc --disable-osx \
                            --enable-video4linux2 --enable-fbdev --with-gfxdrivers="omap,pvr2d"')
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("docs/html/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "TODO", "fb.modes")
