#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())



def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("-k check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doexe("gettext-tools/misc/gettextize", "/usr/bin")


    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "HACKING", "NEWS", "README*", "THANKS")

