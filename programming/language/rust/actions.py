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
    shelltools.system("python ./x.py build")
    #shelltools.system("python ./x.py doc")
    

def install():
    shelltools.system("python ./x.py install")
    #pisitools.insinto("/", "build/x86_64-unknown-linux-gnu/stage0/etc")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage2/bin")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage2/lib")
    #pisitools.insinto("/usr/bin", "build/x86_64-unknown-linux-gnu/stage2-tools-bin/*")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/share")
    #pisitools.insinto("/usr/share/doc/rust/", "build/tmp/dist/rust-docs-1.23.0-x86_64-unknown-linux-gnu/rust-docs/share/doc/rust/*")

