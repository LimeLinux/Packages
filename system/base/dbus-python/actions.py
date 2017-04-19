#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
  

py2dir = "py2build"
py3dir = "py3build"

def configure(pvers, flags):
    shelltools.system("PYTHON=%s ../configure %s" % (pvers, flags))

def setup():
    autotools.autoreconf("-fi")
    confFlags = "--prefix=/usr \
                 --localstatedir=/var \
                 --docdir=/usr/share/doc/python-dbus"
    shelltools.makedirs(py2dir)
    shelltools.cd(py2dir)
    configure ("/usr/bin/python", confFlags)
    shelltools.cd("..")
    shelltools.makedirs(py3dir)
    shelltools.cd(py3dir)
    configure("/usr/bin/python3", confFlags)

def build():
    shelltools.cd(py2dir)
    autotools.make ()
    shelltools.cd("..")
    shelltools.cd(py3dir)
	
def install():
    shelltools.cd(py2dir)
    autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    shelltools.cd(py3dir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
