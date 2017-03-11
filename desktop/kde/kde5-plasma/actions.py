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
names = ["kde-cli-tools", 
        "kdecoration",
        "libkscreen",
        "libksysguard",
        "breeze",
        "breeze-gtk",
        "kscreenlocker",
        "oxygen",
        "kinfocenter",
        "ksysguard",
        "kwin",
        "systemsettings",
        "plasma-workspace",
        "bluedevil",
        "kde-gtk-config",
        "khotkeys",
        "kmenuedit",
        "kscreen",
        "kwallet-pam",
        "kwayland-integration",
        "kwrited",
        "milou",
        "plasma-nm",
        "plasma-pa",
        "plasma-workspace-wallpapers",
        "polkit-kde-agent-1",
        "powerdevil",
        "plasma-desktop",
        "kdeplasma-addons",
        "kgamma5",
        "ksshaskpass",
        "plasma-sdk",
        "sddm-kcm",
        "user-manager",
        "discover",
        "breeze-grub",
        "breeze-plymouth", 
        "kactivitymanagerd",
        "plasma-integration",
        "plasma-tests"] 

def setup():
     shelltools.cd("kwin-%s"% get.srcVERSION())
     shelltools.system("patch -p1 < disable_qpa.patch")
     shelltools.cd("..")
    
def build():
    pass

def install():
	for packs in names:
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
    
    
    
