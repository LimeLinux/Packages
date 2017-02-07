#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sysvinit-%sdsf" % get.srcVERSION()

def build():
    autotools.make("-C src CC=\"%s\" CFLAGS=\"%s -D_GNU_SOURCE\" LCRYPT=\"-lcrypt\"" % (get.CC(), get.CFLAGS()))

def install():
    shelltools.cd("src")
    autotools.rawInstall("ROOT='%s' STRIP=/bin/true" % get.installDIR())

    pisitools.remove("/bin/pidof")
    pisitools.dosym("killall5", "/sbin/pidof")
    pisitools.remove ("/usr/share/man/man8/telinit.8")
    pisitools.remove ("/sbin/reboot")
    pisitools.remove ("/sbin/poweroff")
    pisitools.remove ("/sbin/halt")
    pisitools.remove ("/sbin/shutdown")
    pisitools.remove ("/usr/share/man/man8/shutdown.8")
    pisitools.remove ("/usr/share/man/man8/poweroff.8")
    pisitools.remove ("/usr/share/man/man8/runlevel.8")
    pisitools.remove ("/usr/share/man/man8/halt.8")
    pisitools.remove ("/usr/share/man/man8/reboot.8")
