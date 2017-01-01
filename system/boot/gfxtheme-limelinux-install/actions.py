#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/gfxtheme/limelinux"

def build():
    autotools.make('PRODUCT="LimeLinux"')

def install():
    pisitools.insinto(datadir, "isolinux", "install")
    #pisitools.insinto(datadir, "bootlogo", "install")

