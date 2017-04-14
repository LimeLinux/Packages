#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools , shelltools , get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/lib/libGLESv1_CM.so")
    pisitools.remove("/usr/lib/libGLESv2.so.2.0.0")
    pisitools.remove("/usr/lib/libGLESv1_CM.so.1")
    pisitools.remove("/usr/lib/libGLESv2.so")
    pisitools.remove("/usr/lib/libGLESv2.so.2")
    
    pisitools.dodoc("README.md", "LICENSE")
