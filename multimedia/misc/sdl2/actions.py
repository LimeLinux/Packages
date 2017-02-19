#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL2-%s" % get.srcVERSION()
docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.system("./autogen.sh")

    options = "--enable-sdl-dlopen \
               --disable-arts \
               --disable-esd \
               --disable-nas \
               --enable-alsa \
               --enable-pulseaudio-shared \
               --enable-video-directfb \
               --enable-video-wayland \
               --enable-ibus \
               --enable-fcitx \
               --disable-rpath"


    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("BUGS*", "CREDITS*", "README*", "README-SDL.txt", "TODO*", "WhatsNew*")
