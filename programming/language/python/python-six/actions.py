#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="six-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()


def install():
    pythonmodules.install()




