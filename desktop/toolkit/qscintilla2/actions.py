#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import qt5

WorkDir = "QScintilla_gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]

def setup():
    shelltools.cd("Qt4Qt5")
    shelltools.system("qmake qscintilla.pro")


def build():
    shelltools.cd("Qt4Qt5")
    autotools.make()



def install():
    shelltools.cd("Qt4Qt5")
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())


