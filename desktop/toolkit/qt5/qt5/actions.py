#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

import os

WorkDir = "qt-everywhere-opensource-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)


def setup():
    checkdeletepath="%s/qtbase/src/3rdparty"  % absoluteWorkDir
    for dir in ('libjpeg', 'freetype', 'libpng', 'zlib', "xcb", "sqlite"):
        if os.path.exists(checkdeletepath+dir):
            shelltools.unlinkDir(checkdeletepath+dir)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")


    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    shelltools.system("unset QMAKESPEC")
    shelltools.export("QT5DIR", get.curDIR())
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), get.ENV("PATH")))
    
    
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    shelltools.system('parameters="QMAKE_CFLAGS_ISYSTEM= "')

    options = "-confirm-license -opensource \
		    -prefix /usr \
		    -docdir /usr/share/doc/qt5 \
		    -plugindir /usr/lib/qt5/plugins \
		    -importdir /usr/lib/qt5/imports \
            -qmldir /usr/lib/qt5/qml \
		    -datadir /usr/share/qt5 \
		    -translationdir /usr/share/qt5/translations \
		    -sysconfdir /etc \
		    -examplesdir /usr/share/doc/qt5/examples \
		    -system-sqlite \
		    -system-zlib \
		    -system-libpng \
		    -system-libjpeg \
		    -nomake examples \
            -no-sql-mysql \
		    -no-rpath \
		    -openssl-linked \
		    -silent \
		    -optimized-qmake \
		    -dbus \
		    -reduce-relocations \
		    -no-separate-debug-info \
		    -opengl \
		    -skip qtwebengine \
		    -glib"


    autotools.rawConfigure(options)

def build():
    shelltools.system("unset QMAKESPEC")
    shelltools.export("QT5DIR", get.curDIR())
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), get.ENV("PATH")))
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    autotools.make()

def install():
    shelltools.system("unset QMAKESPEC")
    shelltools.export("QT5DIR", get.curDIR())
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), get.ENV("PATH")))
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dosym("/usr/bin/lrelease", "/usr/bin/lrelease-qt5")
    




