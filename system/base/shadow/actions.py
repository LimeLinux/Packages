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
    autotools.configure("--enable-shadowgrp \
                         --without-selinux \
                         --without-audit \
                         --without-libcrack \
                         --with-libpam \
                         --with-sha-crypt \
                         --enable-nls \
                         --with-group-name-max-length=32 \
                         --disable-shared")
def build():
    # Rebuild gmo catalogs
    autotools.make("-C po update-gmo")

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/", "etc/login.access")
    shelltools.chmod("%s/etc/login.access" % get.installDIR(), 0600)

    pisitools.insinto("/etc/", "etc/limits")
    shelltools.chmod("%s/etc/limits" % get.installDIR(), 0644)

    # groups come from coreutils package
    pisitools.remove("/usr/share/man/man1/groups.1")
    pisitools.remove("/bin/groups")

   # transferred to util-linux
    pisitools.remove("/usr/share/man/man3/getspnam.3")
    pisitools.remove("/usr/share/man/man5/passwd.5")
   


    # Conflicts with man-pages
    pisitools.remove("/bin/su")
    pisitools.remove("/bin/login")
    pisitools.remove("/usr/bin/chsh")
    pisitools.remove("/sbin/nologin")
    pisitools.remove("/usr/bin/chfn")
    pisitools.remove("/usr/sbin/vigr")
    pisitools.remove("/usr/sbin/vipw")
    pisitools.remove("/usr/bin/newgrp")
    pisitools.remove("/usr/share/man/man1/su.1")
    pisitools.remove("/usr/share/man/man1/chfn.1")
    pisitools.remove("/usr/share/man/man8/vipw.8")
    pisitools.remove("/usr/share/man/man8/vigr.8")
    pisitools.remove("/usr/share/man/man1/chsh.1")
    pisitools.remove("/usr/share/man/man1/login.1")
    pisitools.remove("/usr/share/man/man1/newgrp.1")
    pisitools.remove("/usr/share/man/man8/nologin.8")


    pisitools.dodoc("ChangeLog","README","NEWS")

