# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("configure.ac", "pthread-stubs", deleteLine=True)
    autotools.autoreconf("-fi")
    
    
    options = " --prefix=/usr \
                --enable-udev"
		
    if get.ARCH() == 'armv7h':

	options += " --enable-omap-experimental-api --enable-exynos-experimental-api --enable-tegra-experimental-api"
	
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README")
