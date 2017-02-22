#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():   
    autotools.autoreconf("-fiv")
    
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --disable-gtk-doc \
                         --with-included-modules=basic-fc \
                         --%sable-introspection" % ("dis" if get.buildTYPE()=="emul32" else "en"))

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodir("/etc/pango")
    shelltools.touch(get.installDIR() +"/etc/pango/pango.modules")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "README", "NEWS")
