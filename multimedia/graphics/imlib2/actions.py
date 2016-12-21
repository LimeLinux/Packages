#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#optimizationtype = "--enable-amd64" if get.ARCH() == "x86_64", "--enable-asd" if get.ARCH() == "armv7h" else "--enable-mmx"


if get.ARCH() == 'x86_64':
       optimizationtype = " --enable-amd64"
       
elif get.ARCH() == 'armv7h':
       optimizationtype = " "
        
else:
    optimizationtype = " --enable-mmx"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --with-x \
                         --with-jpeg \
                         --with-png \
                         --with-tiff \
                         --with-gif \
                         --with-zlib \
                         --with-bzip2 \
                         %s \
                         --enable-visibility-hiding" % optimizationtype)
     
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")