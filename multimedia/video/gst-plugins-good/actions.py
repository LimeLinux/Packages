#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --disable-esd \
                         --disable-rpath \
                         --with-package-name='LimeLinux gstreamer-plugins-good package' \
                         --with-package-origin='http://www.limelinux.com' \
                         --disable-schemas-install")


    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "README", "RELEASE")
