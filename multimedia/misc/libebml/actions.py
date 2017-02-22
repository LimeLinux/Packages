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
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())
    autotools.configure()

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.install("libdir=%s/usr/lib" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("LICENSE.*")
