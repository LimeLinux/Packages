#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "--prefix=/usr         \
               --sysconfdir=/etc     \
               --localstatedir=/var  \
               --libexecdir=/usr/libexec \
               --disable-static \
               --disable-bluez4 \
               --enable-largefile \
               --disable-tcpwrap \
               --with-database=tdb \
               --with-udev-rules-dir=/lib/udev/rules.d"


    autotools.configure(options)


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "LICENSE", "GPL", "LGPL")
