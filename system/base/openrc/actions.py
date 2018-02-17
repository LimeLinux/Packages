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

args = 'BRANDING="LimeLinux" \
            MKSELINUX=no \
            MKTERMCAP=ncurses \
            PKG_PREFIX=""\
            LIBDIR=/usr/lib \
            SHLIBDIR=/usr/lib \
            LIBEXECDIR=/usr/lib/openrc \
            BINDIR=/usr/bin \
            SBINDIR=/sbin \
	        INCLUDEDIR=/usr/include \
            MKSYSVINIT=yes \
            SYSCONFDIR=/etc'
                

def build():
    autotools.make("%s"% args)

def install():
    autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(),args))

    pisitools.insinto("/etc", "support/sysvinit/inittab")
    pisitools.dosym("/sbin/openrc-init", "/sbin/telinit")


    pisitools.dosym("/etc/init.d/agetty", "/etc/init.d/agetty.tty1")
    pisitools.dosym("/etc/init.d/agetty", "/etc/init.d/agetty.tty2")
    pisitools.dosym("/etc/init.d/agetty", "/etc/init.d/agetty.tty3")
    pisitools.dosym("/etc/init.d/agetty", "/etc/init.d/agetty.tty4")
    pisitools.dosym("/etc/init.d/agetty", "/etc/init.d/agetty.tty5")
    pisitools.dosym("/etc/init.d/agetty", "/etc/init.d/agetty.tty6")


    pisitools.dodoc("LICENSE*", "*guide.*", "AUTHORS", "ChangeLog", "README.*")

