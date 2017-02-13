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


    #util-linux

    pisitools.remove ("/usr/bin/mesg")
    pisitools.remove ("/usr/bin/wall")
    pisitools.remove ("/usr/bin/last")
    pisitools.remove ("/sbin/sulogin")
    pisitools.remove ("/usr/bin/lastb")
    pisitools.remove ("/bin/mountpoint")
    pisitools.remove ("/usr/bin/utmpdump")
    pisitools.remove ("/usr/share/man/man1/mesg.1")
    pisitools.remove ("/usr/share/man/man1/wall.1")
    pisitools.remove ("/usr/share/man/man8/sulogin.8")
    pisitools.remove ("/usr/share/man/man1/lastb.1")
    pisitools.remove ("/usr/share/man/man1/last.1")
    pisitools.remove ("/usr/share/man/man1/utmpdump.1")
    pisitools.remove ("/usr/share/man/man1/mountpoint.1")



