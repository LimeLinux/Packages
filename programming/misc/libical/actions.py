#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
			    -DSHARED_ONLY=true \
			    -DCMAKE_INSTALL_PREFIX=/usr \
			    -DCMAKE_INSTALL_LIBDIR=/usr/lib")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
