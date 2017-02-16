#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--exec-prefix=\"\" \
               --sbindir=/sbin \
               --libdir=/usr/lib \
               --enable-split-usr \
	       --enable-manpages \
               --enable-logging \
               --sysconfdir=/etc \
               --libexecdir=/lib  \
               --with-rootprefix=  \
               --with-rootlibdir=/lib \
               --with-rootlibexecdir=/lib/udev \
               --with-rootrundir=/var/run \
               --enable-gudev"

    autotools.autoreconf("-fi")
    autotools.configure(options)

def build():
    autotools.make("all")


def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())


    # create needed directories
    for d in ("", "net", "pts", "shm", "hugepages"):
        pisitools.dodir("/lib/udev/devices/%s" % d)

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    # Install docs
    pisitools.dodoc("COPYING", "NOTES", "README.md")


