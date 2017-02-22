#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
        #autotools.autoreconf("-vfi")
	pisitools.cxxflags.add(" -std=c++11")
        autotools.configure("--disable-static \
                             --disable-rpath")

        pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    pisitools.dodoc("ChangeLog", "COPYING*", "README*", "TODO")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "contrib")

