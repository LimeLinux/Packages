#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
   # autotools.autoreconf("-vif")
    autotools.configure("    --prefix=/usr \
		    --enable-password-save \
		    --mandir=/usr/share/man \
		    --enable-iproute2 \
		    --with-plugindir='/usr/lib/openvpn/' \
		    --enable-x509-alt-username")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS", "README", "ChangeLog", "NEWS")
