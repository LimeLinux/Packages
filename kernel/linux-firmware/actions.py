#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "./"


def setup():
    shelltools.system("git clone https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git")
    shelltools.system("tar xvf %s/linux-firmware-limelinux.tar.xz" %get.workDIR())
    # Remove source files
    shelltools.unlink("linux-firmware/usbdux/*dux")
    shelltools.unlink("linux-firmware/*/*.asm")

    # These + a lot of other firmware are shipped within alsa-firmware
    for fw in ("linux-firmware/ess", "linux-firmware/korg", "linux-firmware/sb16", "linux-firmware/yamaha"):
        shelltools.unlinkDir(fw)

def build():
    shelltools.cd("linux-firmware")
    autotools.make()


def install():
    shelltools.cd("linux-firmware")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/lib/firmware/", "aic94xx-seq/aic94xx-seq.fw")

    # Remove installed and LIC* files from /lib/firmware
    pisitools.remove("/lib/firmware/GPL-3")
    pisitools.remove("/lib/firmware/configure")
    pisitools.remove("/lib/firmware/Makefile")
    pisitools.removeDir("/lib/firmware/aic94xx-seq")
    
    #conflict on alsa-firmware
    #pisitools.remove("/lib/firmware/ctefx.bin")
    pisitools.remove("/lib/firmware/ctspeq.bin")

    # Install LICENSE files
    pisitools.dodoc("WHENCE", "LICENCE.*", "LICENSE.*", "GPL-3")
