#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# LimeLinux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
  



def configure(pvers, flags):
    shelltools.system("git clone https://github.com/llvm-mirror/libclc.git")
    shelltools.cd("libclc")
    shelltools.system("PYTHON=%s ./configure.py %s" % (pvers, flags))

def setup():
    confFlags = "--prefix=/usr"

    configure ("/usr/bin/python", confFlags)

def build():
    shelltools.cd("libclc")
    autotools.make()
	
def install():
    shelltools.cd("libclc")
    autotools.install("DESTDIR=%s" % get.installDIR())
