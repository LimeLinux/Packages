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
    # Make it build with libtool 1.5
    #
    shelltools.export("CFLAGS", "%s -fPIC -O2 -Wall -Wextra -DLUA_COMPAT_5_1" % get.CFLAGS())                          

    #shelltools.system("rm -rf m4/lt* m4/libtool.m4")
    shelltools.system("sed -e 's:truetype/ttf-dejavu:TTF:g' -i modules/visualization/projectm.cpp")
    shelltools.system("sed -e 's|-Werror-implicit-function-declaration||g' -i configure")
    pisitools.cxxflags.add(" -std=gnu++11")
    shelltools.system("./bootstrap")
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")
    autotools.rawConfigure("\
                            --prefix=/usr \
                            --libdir=/usr/lib \
                            --sysconfdir=/etc \
                            --with-default-font-family=Sans \
                            --with-default-monospace-font-family=Monospace \
                            --with-default-font=/usr/share/fonts/dejavu/DejaVuSans.ttf \
                            --with-default-monospace-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                              LUA=lua  \
                              LUAC=luac  \
                              LUA_LIBS='`pkg-config --libs lua`' \
                              RCC=/usr/bin/rcc \
                            --disable-rpath \
                            --enable-faad \
                            --enable-nls \
                            --enable-lirc \
                            --enable-realrtsp \
                            --enable-aa \
                            --enable-upnp \
                            --enable-opus \
                            --enable-sftp \
                            --enable-lua \
                            --enable-decklink \
                            --enable-opencv")



    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j3")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for icon in ("128x128", "48x48", "32x32", "16x16"):
         pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % icon, "share/icons/%s/vlc*.png" % icon)

    pisitools.dodoc("AUTHORS", "THANKS", "NEWS", "README", "COPYING")
