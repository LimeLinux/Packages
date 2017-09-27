#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("python ./x.py --verbose")
    

def install():
    pisitools.insinto("/", "build/x86_64-unknown-linux-gnu/stage0/etc")
    pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/bin")
    pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/lib")
    pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/share")

