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
    pisitools.flags.add("-DUSE_GET_STACKBASE_FOR_MAIN")
    shelltools.system ("rm -rf libtool libtool.m4")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-cplusplus \
                         --enable-large-config \
                         --enable-threads=posix")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "doc/README.linux", "doc/*.html")
    
    pisitools.removeDir("/usr/share/gc")