#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" INSTALL="install -p"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "COPYING", "LICENSE")
