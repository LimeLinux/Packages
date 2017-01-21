#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PyQt5_gpl-%s" % get.srcVERSION()

def setup():   
    pythonmodules.run("configure.py --confirm-license \
                                    --qsci-api \
                                    --sip /usr/bin/sip \
                                    --destdir='/usr/lib/python3.5/site-packages' \
                                    --sip-incdir='/usr/include/python3.5m' \
                                    ")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")

def build():
    autotools.make()

def install():
    shelltools.cd("%s/PyQt5_gpl-%s" % (get.workDIR(),get.srcVERSION()))
    autotools.rawInstall("-C pyrcc DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C pylupdate DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    #pisitools.rename("/usr/lib/qt5/plugins/designer/libpyqt5.so", "libpyqt5.so.0")
    #pisitools.rename("/usr/lib/python2.7/site-packages/dbus/mainloop/pyqt5.so", "pyqt5.so.0")   

    
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("NEWS", "README","LICENSE*")
