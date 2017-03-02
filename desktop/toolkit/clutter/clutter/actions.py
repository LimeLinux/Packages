#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
   #autotools.autoreconf("-vif")
    autotools.configure("--enable-egl-backend \
			    --enable-introspection \
			    --enable-egl-backend \
			    --enable-gdk-backend \
			    --enable-wayland-backend \
			    --enable-x11-backend \
			    --enable-evdev-input \
			    --enable-wayland-compositor \
			    --disable-gtk-doc \
                         --enable-shared ")

    pisitools.dosed("libtool"," -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc("ChangeLog*", "COPYING", "README*", "NEWS")

