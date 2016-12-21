#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    cmaketools.configure()

def build():
    cmaketools.make()


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "README")
    
    #pisitools.dosym("usr/share/pkgconfig/yajl.pc", "usr/lib/pkgconfig/yajl.pc")
    
    pisitools.domove("/usr/share/pkgconfig", "/usr/lib/")