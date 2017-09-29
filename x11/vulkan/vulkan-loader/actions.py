#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools, cmaketools


def setup():
    shelltools.system("./update_external_sources.sh")
    
    shelltools.system("cmake \
                      -H. -Bdbuild -DCMAKE_INSTALL_PREFIX=/usr \
                      -DCMAKE_INSTALL_LIBDIR=lib \
                      -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                      -DCMAKE_INSTALL_DATADIR=/usr/share \
                      -DCMAKE_SKIP_RPATH=True \
                      -DCMAKE_BUILD_TYPE=Release")

def build():
    shelltools.cd("./dbuild")
    cmaketools.make()

def install():
    shelltools.cd("./dbuild")
    cmaketools.install("DESTDIR='%s'" % get.installDIR())
    
    shelltools.cd()
    pisitools.dodoc("README.md", "COPYRIGHT.txt", "LICENSE.txt", "CONTRIBUTING.md")
    


