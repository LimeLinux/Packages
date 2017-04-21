#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import pisitools, get, shelltools, autotools


WorkDir = "node-%s" % get.srcVERSION()



def setup():
    shelltools.system("python configure --prefix=/usr")

def build():
    autotools.make()

def check():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "CHANGELOG.md", "README*", "LICENSE", "CONTRIBUTING.md")
