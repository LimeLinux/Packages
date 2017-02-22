#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp.service")
    shelltools.system("sed -i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp-sesman.service")
    
    shelltools.system("sed -i 's|/usr/local/sbin|/usr/bin|' instfiles/xrdp.sh")
    shelltools.system("sed -i 's|/usr/sbin|/usr/bin|' instfiles/xrdp.service")
    shelltools.system("sed -i 's|/usr/sbin|/usr/bin|' instfiles/xrdp-sesman.service")
    shelltools.system("./bootstrap")
    
    
    autotools.configure("--enable-jpeg \
			--sbindir=/usr/bin \
                        --enable-fuse")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")
