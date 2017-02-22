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
    shelltools.export("CFLAGS","%s -fwrapv" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

#def check():
#   autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("README","BUGS","ChangeLog","NEWS","THANKS")
