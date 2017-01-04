#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
                        --localstatedir=/var \
                        --libexecdir=/usr/lib/dbus-1.0 \
                        --with-dbus-user=dbus \
                        --with-system-pid-file=/run/dbus/pid \
                        --with-system-socket=/run/dbus/system_bus_socket \
                        --with-console-auth-dir=/run/console/ \
                        --enable-inotify \
                        --disable-dnotify \
                        --disable-verbose-mode \
                        --disable-static \
                        --disable-tests \
                        --disable-asserts")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    # needs to exist for the system socket
    pisitools.dodir("/run/dbus")
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/")







