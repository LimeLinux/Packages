#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "openssh-%s" % get.srcVERSION().replace("_","")

def setup():
   autotools.configure("--sysconfdir=/etc/ssh \
                         --libexecdir=/usr/libexec/ssh \
                         --disable-strip \
                         --with-tcp-wrappers \
                         --with-md5-passwords \
                         --with-ipaddr-display \
                         --with-pam \
                         --with-privsep-user=nobody \
                         --with-privsep-path=/var/empty \
                         --without-zlib-version-check \
                         --without-ssl-engine")



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # fixes #10992
    pisitools.dobin("contrib/ssh-copy-id")
    pisitools.doman("contrib/ssh-copy-id.1")


    pisitools.dodir("/var/empty/sshd")

    pisitools.dodoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
