#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-fi")
    
    autotools.configure("--disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/")
    pisitools.dodoc("AUTHORS","BUGS","ChangeLog","NEWS","doc/*.txt")
