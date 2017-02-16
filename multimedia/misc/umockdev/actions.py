#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools , shelltools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()
    
def build():
    autotools.make()

def install():
    autotools.install()

