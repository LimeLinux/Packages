#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --disable-rpath \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.install()
