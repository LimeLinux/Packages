#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    # Empty
    pisitools.removeDir("/usr/lib/libmcrypt")

    pisitools.dodoc("ChangeLog","COPYING.LIB","KNOWN-BUGS","NEWS","README")
