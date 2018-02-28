#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 Lime Linux
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./configure --prefix=/usr           \
                         -Dbindir=/sbin          \
                         -Dsbindir=/sbin         \
                         -Dpamlibdir=/lib/security \
                         -Dlibdir=/usr/lib       \
                         -Dsysconfdir=/etc       \
                         -Dlibexecdir=/lib       \
                         -Dwith-rootprefix=      \
                         -Dwith-rootlibdir=/lib  \
                         -Dwith-udevrulesdir=/etc/udev/rules.d \
                          ")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    # Install docs
    pisitools.dodoc("README", "TODO", "LICENSE.GPL2", "LICENSE.LGPL2.1", "NEWS")


