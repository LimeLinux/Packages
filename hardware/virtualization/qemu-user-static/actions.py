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
    shelltools.system("ar x qemu-user-static_%s+dfsg-4~bpo8+1_amd64.deb" % get.srcVERSION())
    shelltools.system("tar -xJf data.tar.xz")


def install():
    pisitools.insinto("/usr","usr/*")
    shelltools.makedirs("%s/var/lib/binfmts" % get.installDIR())


