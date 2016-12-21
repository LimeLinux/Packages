#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

args = 'BRANDING="PisiGNU/Linux" \
            MKSELINUX=no \
            MKTERMCAP=ncurses \
            PKG_PREFIX=""\
            LIBDIR=/usr/lib \
            SHLIBDIR=/usr/lib \
            LIBEXECDIR=/usr/lib/openrc \
            BINDIR=/usr/bin \
            SBINDIR=/sbin \
	    INCLUDEDIR=/usr/include \
            SYSCONFDIR=/etc'
                

def build():
    autotools.make("%s"% args)

def install():
    autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(),args))

    pisitools.insinto("/etc", "support/sysvinit/inittab")

    pisitools.dodoc("LICENSE*", "*guide.*", "AUTHORS", "ChangeLog", "README.*")

