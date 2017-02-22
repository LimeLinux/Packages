#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # write sed commands using pisitools.dosed :)
    shelltools.system('sed -i "/^SUBDIRS/s/locate//" Makefile.in')


  #  shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())

    autotools.configure()

def build():
    autotools.make("-C locate dblocation.texi")
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
