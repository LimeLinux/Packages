#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    
    #shelltools.export("QT5LINK", "/usr/lib/qt5/bin")
    #shelltools.export("QT5DIR", "/usr/lib/qt5")
   # shelltools.export("CFLAGS", "%s -I/usr/lib/sqlite3.11.0.0" % get.CFLAGS())
    shelltools.system("qmake WEBENGINE_CONFIG+=use_proprietary_codecs ../qtwebengine.pro")
    
def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR()) 


   # pisitools.dodoc("LICENSE.LGPLv3")
