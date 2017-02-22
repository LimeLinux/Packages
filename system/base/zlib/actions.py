#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get



def setup():
    autotools.rawConfigure("--libdir=/usr/lib \
                            --includedir=/usr/include \
                            --prefix=/usr")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "doc/*", "examples/*")

