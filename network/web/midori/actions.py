#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

shelltools.export("LC_ALL", "C")
WorkDir = "."

def setup():
    shelltools.cd('midori-%s' %(get.srcVERSION()) )
    autotools.rawConfigure("--prefix=/usr")
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON -DCMAKE_SKIP_INSTALL_RPATH=ON")
    

def build():
    shelltools.cd('midori-%s' %(get.srcVERSION()) )
    cmaketools.make()


def install():
    shelltools.cd('midori-%s' %(get.srcVERSION()) )
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

