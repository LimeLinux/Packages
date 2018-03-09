#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-i")
    autotools.configure("--sbindir=/sbin \
                         --enable-compat-symlinks")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s"%get.installDIR())
