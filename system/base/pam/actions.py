#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --disable-audit")
    
def build():
    autotools.make()



def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/Linux-PAM/")

    pisitools.doman("doc/man/*.[0-9]")
    pisitools.dodoc("CHANGELOG", "Copyright", "README")
    
    
    shelltools.cd("/usr/lib/security")
    pisitools.dosym("pam_unix.so", "/usr/lib/security/pam_unix_acct.so")
    pisitools.dosym("pam_unix.so", "/usr/lib/security/pam_unix_auth.so")
    pisitools.dosym("pam_unix.so", "/usr/lib/security/pam_unix_passwd.so")
    pisitools.dosym("pam_unix.so", "/usr/lib/security/pam_unix_session.so")
    
    
