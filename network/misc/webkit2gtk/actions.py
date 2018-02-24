#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools


def setup():
    cmaketools.configure("-G Ninja \
                          -DPORT=GTK \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DENABLE_GTKDOC=ON \
                          -DLIBEXEC_INSTALL_DIR=/usr/lib \
                          -DLIB_INSTALL_DIR=/usr/lib")

def build():
    shelltools.system("ninja")

def install():
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    pisitools.dodoc("NEWS")
