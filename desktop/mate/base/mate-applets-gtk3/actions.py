#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/${_pkgbase} \
                         --enable-polkit \
                         --enable-ipv6 \
                         --with-gtk=3.0 \
                          --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/usr/share/") 
    pisitools.removeDir("/etc/dbus-1/system.d/")
    pisitools.removeDir("/etc/sound/events/") 
    pisitools.removeDir("/usr/bin/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
