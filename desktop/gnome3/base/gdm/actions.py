#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-profiling \
                         --enable-console-helper \
                         --without-plymouth \
			 --without-tcp-wrappers \
                         --disable-scrollkeeper")

    pisitools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.removeDir("/var")
    
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")