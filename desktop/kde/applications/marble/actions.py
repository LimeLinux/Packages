#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DKDE_INSTALL_SYSCONFDIR=/etc \
    -DQT_PLUGINS_DIR=lib/qt/plugins \
    -DBUILD_TESTING=OFF \
    -DBUILD_MARBLE_EXAMPLES=OFF \
    -DBUILD_MARBLE_TESTS=OFF \
    -DMOBILE=OFF")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("BUGS", "ChangeLog", "CODING", "COPYING*", "CREDITS", "LICENSE*", "MANIFESTO.txt", "USECASES")
