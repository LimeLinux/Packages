#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.cd("src")
    autotools.configure("--prefix=/usr --sysconfdir=/etc")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    pisitools.dobin("reaver")
    pisitools.dobin("wash")
    pisitools.insinto("/etc/reaver", "reaver.db")
    shelltools.cd("../docs")
    pisitools.dodoc("README")
    pisitools.doman("reaver.1.gz")