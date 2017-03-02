#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():

    shelltools.system("git clone git://git.drogon.net/wiringPi")

    shelltools.cd("wiringPi")
    
    shelltools.system("sed -i 's|/usr/local/bin/gpio|/usr/bin/gpio|' wiringPi/wiringPi.c")

def build():
    shelltools.cd("wiringPi")
    autotools.make("-C wiringPi all static")
    autotools.make('-C devLib all static INCLUDE+="-I%s/wiringPi" LDFLAGS+="-L%s/wiringPi"'% (get.curDIR(), get.curDIR()))
    
    autotools.make('-C gpio INCLUDE+="-I%s/wiringPi -I%s/devLib" LDFLAGS+="-L%s/wiringPi -L%s/devLib"'% (get.curDIR(), get.curDIR(),get.curDIR(), get.curDIR()))
		    

def install():
    shelltools.cd("wiringPi/wiringPi")
    pisitools.dolib_so("libwiringPi.so*")
    pisitools.dolib_a("libwiringPi.a")
    pisitools.insinto("/usr/include", "*.h")
    pisitools.dosym("/usr/lib/libwiringPi.so.2.32", "/usr/lib/libwiringPi.so")
    
    shelltools.cd("../../wiringPi/devLib")
    pisitools.dolib_so("libwiringPiDev.so*")
    pisitools.dolib_a("libwiringPiDev.a")
    pisitools.insinto("/usr/include", "*.h")
    pisitools.dosym("/usr/lib/libwiringPiDev.so.2.32", "/usr/lib/libwiringPiDev.so")
    
    
    shelltools.cd("../../wiringPi/gpio")
    pisitools.dobin("gpio")
    pisitools.doman("gpio.1")
    
