#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make("mrproper")
    autotools.make("headers_check")

def install():
    autotools.make("INSTALL_HDR_PATH=%s/usr headers_install" % get.installDIR())


