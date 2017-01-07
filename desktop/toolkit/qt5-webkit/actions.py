#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get


def setup():   
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("qmake ../WebKit.pro")

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR()) 


   # pisitools.dodoc("LICENSE.GPLv2", "LICENSE.LGPLv3", "LICENSE.LGPLv21", "ChangeLog-2012-05-22")
