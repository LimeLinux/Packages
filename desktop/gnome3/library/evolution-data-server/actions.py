#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.flags.add("-fPIC -fno-strict-aliasing")

    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib/evolutiondataserver \
                         --enable-vala-bindings \
			 --disable-google-auth \
			 --disable-goa \
                         --disable-uoa")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")     

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README", "TODO")