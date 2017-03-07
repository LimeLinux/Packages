#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    shelltools.system("python waf configure --prefix=/usr --libdir=/usr/lib/")

def build():
    shelltools.system("python waf build -v")

def install():
    shelltools.system("DESTDIR=%s python waf install" % get.installDIR())

    pisitools.dodoc("NEWS", "COPYING", "README")
    pisitools.remove("/usr/bin/lv2specgen.py")
    pisitools.removeDir("/usr/bin/")
    pisitools.removeDir("/usr/share/lv2specgen/")