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
    

    pisitools.domove("/usr/lib/libGLESv*", "/usr/lib/libglvnd")
    pisitools.domove("/usr/lib/libEGL*", "/usr/lib/libglvnd")
    pisitools.domove("/usr/lib/libGL.*", "/usr/lib/libglvnd")


    
    pisitools.dodoc("README.md", "LICENSE")
