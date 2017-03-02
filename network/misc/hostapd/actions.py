#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def build():
    shelltools.cd("hostapd")
    autotools.make()

def install():
    pisitools.dodoc("README","COPYING")
    pisitools.dodir("/etc/hostapd/hostapd")
    shelltools.cd("hostapd")
    pisitools.dodoc("hostapd.*","wired.conf", "hlr_auc_gw.milenage_db")
    
    pisitools.dosbin("hostapd")
    pisitools.dosbin("hostapd_cli")
    pisitools.doman("hostapd.8")
    pisitools.doman("hostapd_cli.1")
