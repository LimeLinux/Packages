#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
   # autotools.autoreconf()
  #  autotools.autoreconf("-vif")
   # shelltools.system("NOCONFIGURE=1 ./autogen.sh")
  #  pisitools.ldflags.add(" -lwrap")
   # autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
			--with-embedded-crypto \
			--with-ivykis=internal \
				--disable-java \
				--disable-docs \
				--enable-manpages \
				--disable-python \
				--with-embedded-crypto \
				--with-ivykis=internal \
				--with-libmongo-client=internal \
				--sysconfdir=/etc/syslog-ng \
				--localstatedir=/var/lib/syslog-ng \
				--with-pidfile-dir=/var/run \
				--with-module-dir=/usr/lib/syslog-ng \
			--with-libmongo-client=internal")
			
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")		


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/libexec")

  #  pisitools.dodoc("COPYING*", "README", "AUTHORS", "ChangeLog")
    
