#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/usr/share/qemu"]

shelltools.export("LC_ALL", "C")

def setup():
    autotools.rawConfigure("--prefix=/usr \
			    --sysconfdir=/etc \
			    --localstatedir=/var \
			    --libexecdir=/usr/lib \
			    --python=/usr/bin/python \
			    --smbd=/usr/bin/smbd \
			    --with-gtkabi=3.0 \
			    --enable-modules \
			    --audio-drv-list='pa alsa sdl'")

def build():
    autotools.make()



def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

  #  pisitools.dobin("qemu-kvm")
    #shelltools.system("chmod u+s %s/usr/lib/qemu/qemu-bridge-helper" % get.installDIR())
   # pisitools.insinto("/etc/sasl2/", "qemu.sasl", "qemu.conf")
    pisitools.removeDir("/var")
    for i in ["pc-bios/README", "LICENSE", "README", "COPYING*", "qemu-doc.html", "qemu-tech.html"]:
        pisitools.dodoc(i)

