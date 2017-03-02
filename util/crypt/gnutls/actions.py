#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    options = "--disable-static \
               --disable-rpath \
               --disable-silent-rules \
               --disable-guile \
               --with-zlib \
                 --without-idn \
                --with-default-trust-store-pkcs11='pkcs11:model=p11-kit-trust;manufacturer=PKCS%2311%20Kit' \
               --disable-valgrind-tests"

    if get.buildTYPE() == "emul32":
        options += " --disable-hardware-acceleration \
                     --enable-local-libopts \
                   "

    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
