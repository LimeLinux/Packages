# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools



WorkDir = "mozilla-esr38/js/src"

def setup():
    pisitools.cxxflags.remove("-fno-delete-null-pointer-checks -fpermissive -fno-tree-vrp -fno-strict-aliasing")
    pisitools.cflags.remove("-fno-delete-null-pointer-checks -fpermissive -fno-tree-vrp -fno-strict-aliasing")
    shelltools.system("export PYTHON=/usr/bin/python2.7")
    #shelltools.system("sed -i 's/(defined\((@TEMPLATE_FILE)\))/\1/' config/milestone.pl ")
    
    autotools.configure("--with-system-nspr \
                         --enable-system-ffi \
                         --with-system-zlib \
                         --with-system-icu \
                         --with-intl-api \
                         --enable-ctypes \
                         --enable-threadsafe \
                         --enable-system-ffi \
                         --enable-shared-js \
                         --enable-gcgenerational \
                         --disable-optimize \
                         --enable-pie")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/bin/js-config", "js38-config")
    pisitools.rename("/usr/bin/js", "js-38")
    pisitools.domove("/usr/include/mozjs-/*" , "/usr/include/mozjs-38")
    pisitools.rename("/usr/lib/pkgconfig/js.pc", "mozjs-38.pc")
    #pisitools.rename("/usr/lib/libmozjs-.so", "libmozjs-38.so")

    
    pisitools.dosym("libmozjs-.so", "/usr/lib/libmozjs-38.so")
    pisitools.removeDir("/usr/include/mozjs-")
    pisitools.doexe("/usr/bin/js", "/usr/bin/js-38")
    
    shelltools.system("sed -i 's/mozjs-/mozjs-38/g' %s/usr/lib/pkgconfig/mozjs-38.pc"% get.installDIR())

