#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

includedir= "/usr/include/wireshark/"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --with-gtk3=yes \
                         --with-pcap \
                         --with-zlib \
                         --with-lua \
                         --with-portaudio \
                         --with-ssl \
                         --with-krb5 \
                         --enable-ipv6 \
                         --with-libsmi \
                         --with-gnu-ld \
                         --with-pic \
                         --with-libcap \
                         --disable-warnings-as-errors \
                         --with-plugins=/usr/lib/wireshark/plugins")
    
    shelltools.system("sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool")
    shelltools.system("sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    for d in ["config.h", "register.h", "ws_symbol_export.h"]:
        pisitools.insinto(includedir, d)
        
    pisitools.insinto("/usr/include/wireshark/epan/", "epan/*.h")
    pisitools.insinto("/usr/include/wireshark/wsutil/", "wsutil/*.h")
    pisitools.insinto("/usr/include/wireshark/wiretap/", "wiretap/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/crypt/", "epan/crypt/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/ftypes/", "epan/ftypes/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/dfilter/", "epan/dfilter/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/dissectors/", "epan/dissectors/*.h")


    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
