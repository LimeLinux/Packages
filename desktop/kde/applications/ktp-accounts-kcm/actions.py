#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import kde5

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.domove("/usr/lib64/*", "/usr/lib")
    pisitools.removeDir("/usr/lib64")
    pisitools.dodoc("COPYING", "INSTALL", "README")
