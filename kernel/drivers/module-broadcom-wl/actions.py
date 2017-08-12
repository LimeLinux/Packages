# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kerneltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = get.ARCH()
KDIR = kerneltools.getKernelVersion()

def build():
    shelltools.system("sed -e '/BRCM_WLAN_IFNAME/s:eth:wlan:' \
		      -i src/wl/sys/wl_linux.c") 
    autotools.make("Werror=0 -C /lib/modules/%s/build M=%s modules" % (KDIR, get.curDIR()))

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KDIR, "wl.ko")

    pisitools.dodoc("lib/LICENSE.txt")