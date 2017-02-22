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
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --with-ui \
                         --with-readline \
                         --enable-nls")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    for f in ("affixcompress", "makealias", "wordforms"):
        pisitools.dobin("src/tools/%s" % f)

    pisitools.dodoc("ABOUT-NLS", "AUTHORS*", "BUGS", "COPYING*", "NEWS", "README*", "THANKS", "TODO")
