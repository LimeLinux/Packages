#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "sip-%s" % get.srcVERSION()

def setup():
    shelltools.system("find . -type f -exec sed -i 's/Python.h/python3.6m\/Python.h/g' {} \;")
    pythonmodules.run('configure.py CFLAGS="%s" CXXFLAGS="%s"' % (get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")
                        

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
