#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "db-%s/build_unix" % get.srcVERSION()

def setup():
   # pisitools.ldflags.add("-Wl,--default-symver -lpthread")
    shelltools.system("../dist/configure \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --datadir=/usr/share \
                       --sysconfdir=/etc \
                       --localstatedir=/var/lib \
                       --libdir=/usr/lib \
                       --enable-compat185 \
                       --enable-shared \
                       --enable-cxx \
                        --enable-stl \
                       --enable-dbm \
                       --disable-tcl \
                       --disable-java \
                       --disable-static \
                       --disable-test")

def build():
    autotools.make("LIBSO_LIBS=-lpthread")

def install():
    autotools.install('libdir="%s/usr/lib"' % get.installDIR())
    pisitools.dosym("/usr/lib/libdb-6.2.so", "/usr/lib/libdb-5.3.so")
    

    # Move docs
    pisitools.domove("/usr/docs/", "/usr/share/doc/%s/html/" % get.srcNAME())
