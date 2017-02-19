#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.cxxflags.add(" -std=c++11")
    shelltools.system("./autogen.sh")
    autotools.configure("./configure \
		                --prefix=/usr \
		                --with-python \
	                	--with-perl \
		                --enable-lcms \
		                --enable-poppler-cairo \
		                --disable-strict-build \
		                --disable-dependency-tracking")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "README")
