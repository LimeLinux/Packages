#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools, shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_LIBDIR=/usr/lib \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DOBS_VERSION_OVERRIDE=21.0.3.1")


def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CONTRIBUTING.rst", "COPYING", "README.rst")
