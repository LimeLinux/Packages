#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Os")
    autotools.make('EFIDIR="/boot/EFI"')


def install():
    pisitools.insinto("/usr/lib", "src/*.o")
    pisitools.insinto("/usr/sbin", "src/efibootdump")
    pisitools.insinto("/usr/sbin", "src/efibootmgr")
    pisitools.insinto("/usr/share/man", "src/*.8")
    pisitools.insinto("/usr/include", "src/include/*.h")
