#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2017 Lime GNU/Linux
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make("BINDIR=/bin")
    

def install():
   
    autotools.install("DESTDIR=%s install" % get.installDIR())
    
    pisitools.dodoc("README.md")


