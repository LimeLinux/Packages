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
    options = " --prefix=/usr \
                --libdir=lib \
                --openssldir=/etc/ssl \
                --enginesdir=/usr/lib/openssl/engines \
                shared -Wa,--noexecstack \
                zlib enable-camellia enable-idea \
                enable-seed enable-tlsext enable-rfc3779 enable-rc5 \
                enable-cms enable-md2 enable-mdc2 threads "
                
    if get.ARCH() == "x86_64":
        options += " enable-ec_nistp_64_gcc_128 linux-x86_64"
        shelltools.system("./Configure  %s" % options)
            
    elif get.ARCH() == "armv7h":
         options += " linux-armv4"
         shelltools.system("./Configure  %s" % options)
         
       
    pisitools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
    pisitools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    autotools.make("depend")
    autotools.make()
    autotools.make("rehash")

def install():
    autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())

    # Rename conflicting manpages
    pisitools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
    pisitools.rename("/usr/share/man/man3/rand.3", "ssl-rand.3")
    pisitools.rename("/usr/share/man/man3/err.3", "ssl-err.3")


    # Move engines to /usr/lib/openssl/engines
    pisitools.dodir("/usr/lib/openssl")
    pisitools.domove("/usr/lib/engines", "/usr/lib/openssl")

    # Certificate stuff
    pisitools.dobin("tools/c_rehash")


    # Create needed dirs
    for cadir in ["misc", "private"]:
        pisitools.dodir("/etc/ssl/%s" % cadir)

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
