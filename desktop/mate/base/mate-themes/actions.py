#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-all-themes   \
                         --enable-test-themes  \
                         --enable-icon-mapping \
                        --with-gtk=2.0 \
                         --enable-test-themes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS")
