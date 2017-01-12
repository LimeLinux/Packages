#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


shelltools.export("LC_ALL", "C")

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib -DUSE_GTK3=0 -G Ninja", sourceDir="..")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")


def install():
    shelltools.system("DESTDIR='%s' ninja -C  '%s/build' install" % (get.installDIR(),get.curDIR()))

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

