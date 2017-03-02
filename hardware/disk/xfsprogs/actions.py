#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", "%s" % get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.configure("--enable-readline=yes \
                         --enable-blkid=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR())
    autotools.rawInstall("DIST_ROOT=%s" % get.installDIR(), "install-dev")

    shelltools.chmod("%s/lib/libhandle.so.*.*.*" % get.installDIR(), 0755)
