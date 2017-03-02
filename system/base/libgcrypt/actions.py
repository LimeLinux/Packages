#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options = "--disable-static \
               --enable-noexecstack"

    autotools.configure(options)

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/gcrypt")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "THANKS", "TODO")
