#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    autotools.configure("\
                         --libexecdir=/usr/lib/GConf \
                         --disable-static \
                         --disable-silent-rules \
                         --enable-defaults-service \
                         --with-gtk=3.0 \
                        ")

def build():
    autotools.make("pkglibdir=/usr/lib/GConf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS")
