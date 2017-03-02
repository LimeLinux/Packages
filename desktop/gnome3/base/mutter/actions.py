#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools, shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-static \
		                 --enable-compile-warnings=minimum \
		                 --enable-gl \
	                 	 --enable-glx \
		                 --enable-sm \
		                 --enable-startup-notification \
		                 --enable-verbose-mode \
	                   	 --enable-xlib-egl-platform \
		                 --with-default-driver=gl \
	        	         --with-libcanberra")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*")
