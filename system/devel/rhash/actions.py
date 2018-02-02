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
    shelltools.export("CFLAGS","%s -fPIC -DPIC" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -fPIC" % get.LDFLAGS())


def build():
    autotools.make("build-shared")
    autotools.make("-C librhash")


def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dolib_so("librhash/librhash.so.0","/usr/lib/")
    pisitools.dosym("librhash.so.0", "/usr/lib/librhash.so")
    pisitools.insinto("/usr/include/","librhash/*.h")

    pisitools.dodoc("ChangeLog", "INSTALL", "README", "COPYING")

