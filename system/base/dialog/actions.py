#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--prefix=/usr \
                    --enable-nls \
                    --with-libtool \
                    --with-ncursesw")
def build():
    autotools.make()

def install():
    autotools.rawInstall("install-full DESTDIR=%s" % get.installDIR())


    pisitools.dodoc("COPYING", "README")
