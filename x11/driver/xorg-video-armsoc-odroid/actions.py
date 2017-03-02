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
    shelltools.system("git clone -b r4p0 git://github.com/mdrjr/xf86-video-armsoc")
    
    shelltools.cd("xf86-video-armsoc")
    shelltools.system("sh autogen.sh --prefix=/usr --with-drmmode=exynos")
    #autotools.configure("--with-drmmode=exynos")
    
def build():
    shelltools.cd("xf86-video-armsoc")
    autotools.make()

def install():
    shelltools.cd("xf86-video-armsoc")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
  #  pisitools.dodoc("NEWS", "README")


