#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    if get.ARCH() == 'armv7h':
	pisitools.flags.add(" -fPIC")
    
    
    pisitools.dosed("unix/vncserver", "iconic", "nowin")
    shelltools.system("cmake -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX=/usr")
    autotools.make()
    shelltools.system("tar -xf ../xorg-server-1.18.0.tar.bz2 -C unix/xserver --strip-components=1")
    shelltools.cd("unix/xserver")
    shelltools.system("patch -Np1 -i ../xserver117.patch")
    autotools.autoreconf("-fiv")
    autotools.configure(" --prefix=/usr \
                        --disable-static --without-dtrace --without-systemd-daemon \
                         --disable-systemd-daemon \
                        --disable-xorg --disable-xnest --disable-xvfb --disable-dmx \
                        --disable-xwin --disable-xephyr --disable-kdrive --disable-xwayland \
                        --disable-config-hal --disable-config-udev --with-pic \
                        --disable-unit-tests --disable-devel-docs --disable-selective-werror \
                        --disable-dri --enable-dri2 --enable-dri3 --enable-glx --enable-glx-tls") 
    
    autotools.make()
    

def install():
    shelltools.cd("unix/xserver")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd ("../..")
    pisitools.dodoc("LICENCE.*", "README.*")
    shelltools.cd ("unix/xserver/hw/vnc")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
