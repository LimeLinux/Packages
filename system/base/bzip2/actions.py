#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

libversion = get.srcVERSION()

def build():
    autotools.make('CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC"' % (get.CC(), get.AR(), get.RANLIB(), get.CFLAGS()))
    autotools.make('CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" -f Makefile-libbz2_so' % get.CFLAGS())



def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    # No static libs
    pisitools.removeDir("/usr/lib")
    pisitools.domove("/usr/bin/", "/")

    for link in ("/bin/bunzip2", "/bin/bzcat"):
        pisitools.remove(link)
        pisitools.dosym("/bin/bzip2", link)

        pisitools.remove("/bin/bzegrep")
        pisitools.remove("/bin/bzfgrep")
        pisitools.remove("/bin/bzless")
        pisitools.remove("/bin/bzcmp")

        pisitools.dosym("/bin/bzgrep", "/bin/bzegrep")
        pisitools.dosym("/bin/bzgrep", "/bin/bzfgrep")
        pisitools.dosym("/bin/bzdiff", "/bin/bzcmp")
        pisitools.dosym("/bin/bzmore", "/bin/bzless")


    pisitools.dolib("libbz2.so.%s" % libversion, "/lib")

    pisitools.dosym("libbz2.so.1", "/lib/libbz2.so")
    pisitools.dosym("libbz2.so.%s" % libversion, "/lib/libbz2.so.1")

    pisitools.dohtml("manual.html")
    pisitools.dodoc("README", "CHANGES", "bzip2.txt")
