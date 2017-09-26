#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    pisitools.flags.add("-D_FILE_OFFSET_BITS=64", "-D_GNU_SOURCE", "-DLDAP_DEPRECATED", "-fPIC")

    autotools.configure("\
                          --sysconfdir=/etc                  \
                          --prefix=/usr                      \
                          --localstatedir=/var               \
                          --with-piddir=/run/samba           \
                          --with-pammodulesdir=/lib/security \
                          --enable-fhs                       \
                          --without-ad-dc                    \
                          --without-systemd                  \
                          --enable-selftest")
    # !ldb,!pyldb-util

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("samba-4.0/libsmbclient.h", "/usr/include/libsmbclient.h")
    
