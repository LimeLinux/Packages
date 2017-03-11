#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	shelltools.system("cmake -DCMAKE_BUILD_TYPE=Release \
			-DCMAKE_INSTALL_PREFIX=/usr \
			-DLIB_INSTALL_DIR=lib \
			-DLIBEXEC_INSTALL_DIR=lib \
			-DPHONON_BUILD_PHONON4QT5=ON \
			-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
			-DQML_INSTALL_DIR=/usr/qml \
			-DBUILD_TESTING=OFF -Wno-dev ..")

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
    
    pisitools.domove("/usr/lib64/*", "/usr/lib/")
    pisitools.removeDir("/usr/lib64")
