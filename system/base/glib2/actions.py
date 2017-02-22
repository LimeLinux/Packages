#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    options = "--with-pcre=system \
               --disable-fam \
               --disable-libelf \
               --enable-gtk-doc=no \
               --disable-static \
               --enable-shared \
               --disable-man \
               --enable-systemtap"



    #autotools.autoreconf("-vif")
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.removeDir("/usr/share/gdb")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")
