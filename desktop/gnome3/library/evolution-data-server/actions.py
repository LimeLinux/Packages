#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools, cmaketools



def setup():
    cmaketools.configure("--disable-static \
                         --libexecdir=/usr/lib/evolutiondataserver \
                         --enable-vala-bindings \
                         --disable-uoa")
    
   

def build():
    cmaketools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README", "TODO")
