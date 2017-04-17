#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    shelltools.system("./update_external_sources.sh")
 
    cmaketools.configure("-DCMAKE_INSTALL_SYSCONFDIR=/etc \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DCMAKE_SKIP_RPATH=True \
                          -DBUILD_TESTS=Off \
                          -DBUILD_WSI_XCB_SUPPORT=On \
                          -DBUILD_WSI_XLIB_SUPPORT=On \
                          -DBUILD_WSI_WAYLAND_SUPPORT=On \
                          -DBUILD_WSI_MIR_SUPPORT=Off \
                          -DCMAKE_BUILD_TYPE=Release \
                          ")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR='%s'" % get.installDIR())

    pisitools.dodoc("README.md", "COPYRIGHT.txt", "LICENSE.txt", "CONTRIBUTING.md")
    


