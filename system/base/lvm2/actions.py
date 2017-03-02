#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    autotools.configure("--with-usrlibdir=/usr/lib\
                        --enable-pkgconfig\
                        --enable-readline \
                        --enable-dmeventd \
                        --enable-cmdlib \
                        --enable-applib \
                        --with-udevdir=/lib/udev/rules.d/ \
                        --enable-udev_sync \
                        --enable-udev_rules")


def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())
    
    autotools.make("-C liblvm DESTDIR=%s install"% get.installDIR())

    autotools.make("DESTDIR=%s install_device-mapper" % get.installDIR())

    pisitools.dodoc("COPYING", "COPYING.LIB", "README", "VERSION", "VERSION_DM", "WHATS_NEW", "WHATS_NEW_DM")
