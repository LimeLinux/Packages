#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("git clone git://github.com/mdrjr/5422_mali")

def install():
    
    shelltools.cd("5422_mali")
    
    pisitools.insinto("/usr/lib/mali-egl", "x11/*")
   # pisitools.insinto("/usr/lib/mali-egl", "fbdev/*")
    pisitools.insinto("/usr/include", "headers/CL*")
    pisitools.dodoc("LICENSE.md")