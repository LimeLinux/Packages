#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="icu/source"

def setup():
    autotools.configure("--with-data-packaging=library")


def build():
    autotools.make()

def check():
    autotools.make("-k check")


def install():
    autotools.rawInstall('-j1 DESTDIR="%s"' % get.installDIR())

    pisitools.dohtml("../*.html")
