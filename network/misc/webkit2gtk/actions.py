#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools



def setup():
    cmaketools.configure("-DPORT=GTK \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_INSTALL_DIR=/usr/lib \
                          -DLIBEXEC_INSTALL_DIR=/usr/lib/webkit2gtk-4.0 \
                          -DENABLE_GTKDOC=ON ")



def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.domove("/usr/share/gtk-doc/html", "/usr/share/doc/webkit-gtk2")

    pisitools.dodoc("NEWS")
