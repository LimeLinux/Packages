#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "libvpx"
# libdir = "lib64" if get.ARCH() == "x86_64" else "lib"
libdir = "lib"

def setup():
    options = "--prefix=/usr \
               --enable-vp8 \
               --enable-vp9 \
               --enable-runtime-cpu-detect \
               --enable-shared \
               --enable-postproc \
               --enable-pic \
               --disable-install-docs \
               --disable-install-srcs"
               
    if get.ARCH() == "armv7h":
        options += " --disable-neon --disable-neon-asm"
        
    shelltools.system("./configure %s" % options)
    
def build():
    autotools.make("verbose=true")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/%s/*.a" % libdir)

    pisitools.dodoc("AUTHORS", "CHANGELOG", "LICENSE", "PATENTS")
