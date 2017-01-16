#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build-gtk2")
    shelltools.makedirs("build-gtk3")
    
    shelltools.cd("build-gtk3")
    shelltools.system(".././configure \
                         --prefix=/usr \
                         --libexecdir=/usr/lib/libindicator \
                         --disable-tests \
                         --disable-static \
                         --with-gtk=3")
    
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    
    shelltools.cd("../build-gtk2")
    shelltools.system(".././configure \
                         --prefix=/usr \
                         --libexecdir=/usr/lib/libindicator \
                         --disable-tests \
                         --disable-static \
                         --with-gtk=2")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    shelltools.cd("build-gtk3")
    autotools.make()
    
    shelltools.cd("../build-gtk2")
    autotools.make()
    
def install():
    shelltools.cd("build-gtk3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("../build-gtk2")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../")
    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "COPYING", "README")
