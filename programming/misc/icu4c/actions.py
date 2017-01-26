#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="icu/source"

def setup():
    autotools.autoconf("-f")
    options = "--with-data-packaging=library \
               --disable-samples \
               --disable-silent-rules"

    autotools.configure(options)
    pisitools.dosed("config/mh-linux", "-nodefaultlibs -nostdlib")

def build():
    autotools.make()


def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dosym("/usr/lib/libicudata.so.58.2","/usr/lib/libicudata.so.55")
    pisitools.dosym("/usr/lib/libicuio.so.58.2","/usr/lib/libicuio.so.55")
    pisitools.dosym("/usr/lib/libicutest.so.58.2","/usr/lib/libicutest.so.55")
    pisitools.dosym("/usr/lib/libicutu.so.58.2","/usr/lib/libicutu.so.55")
    pisitools.dosym("/usr/lib/libicuuc.so.58.2","/usr/lib/libicuuc.so.55")
    pisitools.dosym("/usr/lib/libicui18n.so.58.2","/usr/lib/libicui18n.so.55")

    pisitools.dohtml("../*.html")
