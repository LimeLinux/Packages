#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

WorkDir = "XML-Simple-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()


def install():
    perlmodules.install()
