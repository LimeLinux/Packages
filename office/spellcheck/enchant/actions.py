#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-static \
                         --enable-aspell \
                         --enable-zemberek \
                         --enable-myspell \
                         --with-myspell-dir=/usr/share/hunspell \
                         --disable-ispell \
                         --disable-uspell \
                         --disable-hspell")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO", "HACKING", "MAINTAINERS")
