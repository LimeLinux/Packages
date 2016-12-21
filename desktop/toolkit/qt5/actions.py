#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

import os

WorkDir = "qt-everywhere-opensource-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')


def setup():

    shelltools.system("unset QMAKESPEC")
    shelltools.export("QT5DIR", get.curDIR())
    shelltools.export("PATH", "%s/bin:%s" % (get.curDIR(), get.ENV("PATH")))
    
    
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))

    options = "-confirm-license -opensource \
		    -prefix /usr \
		    -docdir /usr/share/doc/qt5 \
		    -plugindir /usr/lib/qt5/plugins \
		    -importdir /usr/lib/qt5/imports \
		    -datadir /usr/share/qt5 \
		    -translationdir /usr/share/qt5/translations \
		    -sysconfdir /etc \
		    -examplesdir /usr/share/doc/qt5/examples \
		    -plugin-sql-{sqlite,odbc} \
		    -system-sqlite \
		    -system-zlib \
		    -system-libpng \
		    -system-libjpeg \
		    -nomake examples \
		    -no-rpath \
		    -openssl-linked \
		    -silent \
		    -optimized-qmake \
		    -dbus \
		    -reduce-relocations \
		    -no-separate-debug-info \
		    -opengl \
		    -no-openvg \
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
    
    
    
    