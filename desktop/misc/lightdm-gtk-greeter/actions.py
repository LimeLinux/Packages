#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    pisitools.cflags.add(" -fno-builtin-strftime")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-liblightdm-gobject \
                           --with-libxklavier \
                            --enable-kill-on-sigterm \
                            --disable-libido \
                            --disable-libindicator \
                            --disable-static \
                         --disable-gtk-doc ")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
