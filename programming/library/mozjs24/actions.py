# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools



WorkDir = "mozjs-%s/js/src" % get.srcVERSION()

def setup():
    pisitools.cxxflags.remove("-fPIC")
    shelltools.system("sed -i 's/(defined\((@TEMPLATE_FILE)\))/\1/' config/milestone.pl ")
    
    autotools.configure("--with-system-nspr \
                         --enable-system-ffi \
                         --enable-readline \
			 --enable-intl-api \
                         --enable-threadsafe")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/bin/js-config", "js24-config")
    pisitools.rename("/usr/bin/js", "js-24")
    pisitools.domove("/usr/include/mozjs-/*" , "/usr/include/mozjs-24")
    pisitools.rename("/usr/lib/pkgconfig/mozjs-.pc", "mozjs-24.pc")
    #pisitools.rename("/usr/lib/libmozjs-.so", "libmozjs-24.so")
    pisitools.remove("usr/lib/libmozjs-.a")
    
    pisitools.dosym("libmozjs-.so", "/usr/lib/libmozjs-24.so")
    pisitools.removeDir("/usr/include/mozjs-")
    
    shelltools.system("sed -i 's/mozjs-/mozjs-24/g' %s/usr/lib/pkgconfig/mozjs-24.pc"% get.installDIR())