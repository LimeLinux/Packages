#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    
   # shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    shelltools.cd("generate/unix")
    shelltools.system("sed -i -e 's/_CYGWIN/_LINUX/g' -e 's/-Werror//g' Makefile.config")
    autotools.make("clean")
    autotools.make()
def install():
    
    shelltools.cd("generate/unix")
  #  pisitools.dobin("bin/acpi*")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
