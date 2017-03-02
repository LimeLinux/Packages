#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2015 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make("SBINDIR=/sbin RUNSCRIPT=openrc-run")
    

def install():
   
    autotools.make("DESTDIR=%s SYSCONFDIR=/etc install" % get.installDIR())
    
    #pisitools.dodoc("LICENSE.*")


