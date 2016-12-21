#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i '1i #include <sys/stat.h>' src/helpers/job-drive-detach.c")
    #autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
                        --localstatedir=/var \
                        --libexecdir=/usr/lib/udisks \
                        --disable-static \
                        --enable-lvm2 \
                        --disable-gtk-doc \
                        --disable-man-pages")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.move("%s/lib/udev"% get.installDIR(), "%s/usr/lib/udev"% get.installDIR())
    pisitools.removeDir("/lib")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
