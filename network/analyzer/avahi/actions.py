#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():

    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr        \
                        --sysconfdir=/etc    \
                        --localstatedir=/var \
                        --disable-static     \
                        --disable-mono       \
                        --disable-monodoc    \
                        --disable-python     \
                        --disable-qt3        \
                        --disable-gtk3  \
                        --disable-gtk2  \
                         --with-distro=none   \
                        --disable-qt4  \
                        ")
    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Add missing symlinks for avahi-compat-howl and avahi-compat-dns-sd
    pisitools.dosym("/usr/lib/pkgconfig/avahi-compat-howl.pc", "/usr/lib/pkgconfig/howl.pc")
    pisitools.dosym("/usr/lib/pkgconfig/avahi-compat-libdns_sd.pc", "/usr/lib/pkgconfig/libdns_sd.pc")
    pisitools.dosym("/usr/include/avahi-compat-libdns_sd/dns_sd.h", "/usr/include/dns_sd.h")

    pisitools.removeDir("/var")

    pisitools.dodoc("docs/AUTHORS", "docs/README", "docs/TODO")

