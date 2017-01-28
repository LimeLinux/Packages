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

    pisitools.dohtml("../*.html")
