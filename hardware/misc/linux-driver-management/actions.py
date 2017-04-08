#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("./build")
    shelltools.system("meson --prefix=/usr --buildtype=plain --libdir='lib%LIBSUFFIX%' --libexecdir='lib%LIBSUFFIX%/%PKGNAME%' --sysconfdir=/etc --localstatedir=/var -Dwith-gl-driver-switch-compat=true")

def build():
    shelltools.system("ninja -C build")


def install():
    shelltools.cd("./build")
    pisitools.insinto("/usr/bin/","linux-driver-management")
