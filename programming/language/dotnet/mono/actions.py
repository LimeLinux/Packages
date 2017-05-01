#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import glob
import os.path

shelltools.export("LC_ALL", "C")

def setup():
    autotools.autoreconf()

    autotools.configure("--with-mcs-docs=no")

def build():
    autotools.make()

    shelltools.cd("mcs/jay")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("NEWS", "COPYING.LIB", "README.md", "LICENSE")

    shelltools.cd("mcs/jay")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())



    # These work on Windows only
    for i in glob.glob("%s/usr/lib/mono/*/Mono.Security.Win32*" % get.installDIR()):
        x = i.split(get.installDIR())[-1]
        if os.path.isdir(x):
            pisitools.removeDir(x)
            continue

        pisitools.remove(x)

    
