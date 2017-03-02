#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "espeak-%s-source" % get.srcVERSION()

def setup():
    # Build against portaudio v19
    shelltools.copy("src/portaudio19.h", "src/portaudio.h")


def build():
    shelltools.cd("src")
    autotools.make("CXXFLAGS='%s' CFLAGS='%s' LDFLAGS='%s'" % (get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s BINDIR=/usr/bin INCDIR=/usr/include/espeak LIBDIR=/usr/lib" % get.installDIR())
    shelltools.cd("..")

    pisitools.dodoc("ReadMe", "ChangeLog.txt", "License.txt")
