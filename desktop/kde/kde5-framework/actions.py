#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
names = ["extra-cmake-modules",
         "attica",
         "bluez-qt",
         "breeze-icons",
         "kapidox",
         "karchive",
         "kcodecs",
         "kconfig", 
         "kcoreaddons",
         "kdbusaddons",
         "kdnssd",
         "kguiaddons",
         "ki18n",
         "kidletime",
         "kimageformats",
         "kitemmodels",
         "kitemviews",
         "kplotting",
         "kwayland",
         "kwidgetsaddons",
         "kwindowsystem",
         "modemmanager-qt",
         "networkmanager-qt",
         "oxygen-icons5",
         "kfilemetadata",
         "solid",
         "sonnet",
         "threadweaver",
         "kauth",
         "kcrash",
         "kcompletion",
         "kconfigwidgets",
         "kservice",
         "kemoticons",
         "kjobwidgets",
         "kglobalaccel",
         "kdoctools",
         "kiconthemes",
         "kpty",
         "ktextwidgets",
         "kxmlgui",
         "kbookmarks",
         "kunitconversion",
         "kdesu",
         "kidletime",
         "knotifications",
         "kpeople",
         "syntax-highlighting",
         "prison",
         "kwallet",
         "kio",
         "kjs",
         "kjsembed",
         "kpackage",
         "kparts",
         "kdeclarative",
         "khtml",
         "kactivities",
         "kactivities-stats",
         "kcmutils",
         "kinit",
         "knewstuff",
         "frameworkintegration",
         "kded",
         "kross",
         "plasma-framework",
         "krunner",
         "kdewebkit",
         "kxmlrpcclient",
         "knotifyconfig",
         "kmediaplayer",
         "kdesignerplugin",
         "baloo",
         "kdelibs4support",
         "ktexteditor"]


def setup():
    pass
def build():
    pass

def install():
	for packs in names:
		#pisitools.cxxflags.add(" -std=c++11 -std=c99")
		shelltools.export("LDFLAGS", "%s -I%s/usr/include -I%s/usr/lib/cmake -I%s/usr/share" % (get.LDFLAGS(),get.installDIR(),get.installDIR(),get.installDIR()))
		shelltools.export("CXXFLAGS", "%s -I%s/usr/include -I%s/usr/lib/cmake -I%s/usr/share" % (get.CXXFLAGS(),get.installDIR(),get.installDIR(),get.installDIR()))
		
		shelltools.cd("%s-%s" %(packs,get.srcVERSION()))
		shelltools.makedirs("build")
		shelltools.cd("build")
		shelltools.system("cmake -DCMAKE_BUILD_TYPE=Release \
			-DCMAKE_INSTALL_PREFIX=/usr \
			-DLIB_INSTALL_DIR=lib \
			-DLIBEXEC_INSTALL_DIR=lib \
			-DCMAKE_PREFIX_PATH=%s/usr \
			-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
			-DQML_INSTALL_DIR=/usr/qml \
			-DBUILD_TESTING=OFF -Wno-dev .."% get.installDIR())
			
		autotools.make()
		autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
		#pisitools.dodoc("README.*", "COPYING", "AUTHORS", "ChangeLog")
		shelltools.cd("../..")
    
    
    
