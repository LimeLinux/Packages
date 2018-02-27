#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="gsm-1.0-pl17"

def setup():
    multilib = " -m32" if get.buildTYPE() == "emul32" else ""
    pisitools.dosed("Makefile", "limeCC", "%s %s" % (get.CC(), multilib))
    pisitools.dosed("Makefile", "limeCFLAGS", "%s %s" % (get.CFLAGS(), multilib))

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("DESTDIR=%s bindir=/emul32 libdir=/usr/lib32" % get.installDIR())
        pisitools.remove("/usr/lib32/libgsm.a")
        return
    else:
        autotools.rawInstall("DESTDIR=%s bindir=/usr/bin" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYRIGHT", "MACHINES", "MANIFEST", "README")
