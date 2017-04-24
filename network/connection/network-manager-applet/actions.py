#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--enable-gtk-doc \
                         --enable-introspection \
                         --enable-ld-gc \
                         --disable-static \
                         --disable-maintainer-mode \
                         --with-bluetooth \
                         --with-team \
                         --with-wwan \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --prefix=/usr \
                         --libexecdir=/usr/lib/NetworkManager")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("-k check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
