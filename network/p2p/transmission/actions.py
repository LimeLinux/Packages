#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("m4/glib-gettext.m4")
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-cli \
                         --disable-daemon")


def build():
    autotools.make()


def install():

    # gtk
    autotools.rawInstall("-C gtk DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C po DESTDIR=%s" % get.installDIR())

    # cli,web, deamon
    for _dir in ["cli", "web", "utils"]:
        autotools.rawInstall("-C %s DESTDIR=%s" % (_dir, get.installDIR()))

    # For daemon config files.
    pisitools.dodir("/etc/transmission-daemon")

    pisitools.dodoc("COPYING", "AUTHORS", "README", "NEWS")
