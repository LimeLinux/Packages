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
    shelltools.system("./autogen.sh")
    shelltools.system("./configure \
                      --sysconfdir=/etc \
                      --prefix=/usr \
                      --libdir=/usr/lib \
                      --libexecdir=/usr/ \
                      --enable-split-usr \
                      --enable-polkit \
                      --disable-smack \
                      --enable-acl \
                      --enable-pam \
                      --with-rootlibexecdir=/usr/lib/elogind \
                      --with-rootlibdir=/usr/lib \
                      --with-udevrulesdir=/usr/lib/udev/rules.d \
                      ")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

    # Install docs
    pisitools.dodoc("README", "TODO", "LICENSE.GPL2", "LICENSE.LGPL2.1", "NEWS")


