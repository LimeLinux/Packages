#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools





def build():
    shelltools.cd("src/swig/python")
    shelltools.system("sh build")


def install():
    shelltools.cd("src/swig/python")
    pisitools.dolib_so("_mlt.so", "usr/lib/python2.7/")
    pisitools.dolib_so("mlt_wrap.o", "usr/lib/python2.7/")
    pisitools.dolib_so("mlt.py", "usr/lib/python2.7/")
