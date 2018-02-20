#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("printf '%s\n' >>doc/libinput.doxygen.in \
                       HAVE_DOT=yes DOT_IMAGE_FORMAT=svg INTERACTIVE_SVG=yes")
    shelltools.system("meson build --prefix=/usr \
                       --libexecdir=/usr/lib       \
                        ")

def build():
    shelltools.system("ninja -C build")

def install():
    shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())
    pisitools.dosym("libinput.so.10.13.0","/usr/lib/libinput.so.0")
    
    pisitools.dodoc("COPYING","README.*")
