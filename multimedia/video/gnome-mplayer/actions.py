#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# for snapshots only
if "_" in get.srcVERSION():
    WorkDir = "gnome-mplayer"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-nautilus \
                         --disable-gtk3 \
                         --with-libnotify \
                         --disable-schemas-install")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # installing manually since make install causes sandbox violation
    # enable it only if you are using gconf
    # pisitools.insinto("/etc/gconf/schemas/", "gnome-mplayer.schemas")

    pisitools.remove("/%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))
