#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = 'appinfo-%s' % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
