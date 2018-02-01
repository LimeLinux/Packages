#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("meson --buildtype plain build --prefix=/usr")

    

def build():
    shelltools.system("ninja -C build")

def check():
    shelltools.system("python3 -m pytest test")
    

def install(): 
    shelltools.system("DESTDIR='%s' ninja -C  '%s/build' install" % (get.installDIR(),get.curDIR()))

    pisitools.removeDir("/dev")
    pisitools.removeDir("/etc")


    pisitools.dodoc("AUTHORS", "ChangeLog.rst", "COPYING", "README.md")
