#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools , shelltools
from pisi.actionsapi import get

makeargs="prefix=/usr sbindir=/usr/bin mandir=/usr/share/man"

def setup():
    shelltools.system("git clone https://git.ffmpeg.org/rtmpdump.git")
    shelltools.cd("rtmpdump") 
    shelltools.system("sed -e 's/^CRYPTO=OPENSSL/#CRYPTO=OPENSSL/' -e 's/#CRYPTO=GNUTLS/CRYPTO=GNUTLS/' -i Makefile -i librtmp/Makefile")
    pisitools.dosed("Makefile", "CC=.*", "CC=%s" % get.CC())
    pisitools.dosed("Makefile", "LDFLAGS=.*", \
                                "LDFLAGS=%s" % get.LDFLAGS())

    pisitools.dosed("librtmp/Makefile", "CC=.*", \
                                        "CC=%s" % get.CC())


def build():
    shelltools.cd("rtmpdump")  
    autotools.make(' -j1 %s XCFLAGS="%s"' % (makeargs, get.CFLAGS()) )

def install():
    shelltools.cd("rtmpdump")
    autotools.rawInstall(' -j1 %s DESTDIR=%s' % (makeargs, get.installDIR()))

    #pisitools.remove("/usr/lib/librtmp.a")

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "librtmp/COPYING", "librtmp-COPYING")
    pisitools.dodoc("COPYING", "ChangeLog", "README")
