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

docs = ["CONTRIBUTING.md", "README.md", "LICENSE"]

def setup():
    cmaketools.configure("-G Ninja \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIBDIR=/lib")

def build():
    shelltools.system("ninja")

def install():
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
