#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/aclocal/ax_check_enable_debug.m4")
    pisitools.remove("/usr/share/aclocal/ax_code_coverage.m4")

   # pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog*", "NEWS", "README")
