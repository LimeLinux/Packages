#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir = "./"


def setup():
    shelltools.system("git clone git://git.savannah.gnu.org/config.git")
 


def build():
    shelltools.cd("%s/config" % get.workDIR())
    shelltools.system("make check")

def install():
    shelltools.cd("%s/config" % get.workDIR())
    pisitools.doexe("config.*", "/usr/share/gnuconfig")

    pisitools.dodoc("ChangeLog")
