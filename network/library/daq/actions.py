#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

#def setup():
#    autotools.aclocal("-I m4")
#    autotools.autoheader()
#    libtools.libtoolize("--force --copy --automake")
#    autotools.configure("--libdir=/usr/lib")
#    
#    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def setup():
    #autotools.aclocal("-I m4")
    #autotools.autoheader()
    #libtools.libtoolize("--force --copy --automake")
    #autotools.configure("--enable-nfq-module=yes --prefix=/usr --libdir=/usr/lib")
    autotools.configure("--enable-nfq-module=yes --prefix=/usr")
    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
