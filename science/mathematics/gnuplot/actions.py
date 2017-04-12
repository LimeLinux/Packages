#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-gihdir=/usr/share/gnuplot \
                         --with-readline=gnu \
                         --with-X11 \
                         --with-wx-single-threaded ")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    # Docs, Demo, Manual and Tutorial files
    pisitools.insinto("/usr/share/doc/%s/demo" % get.srcNAME(), "demo/*")
    pisitools.remove("/usr/share/doc/%s/demo/Makefile*" % get.srcNAME())
    #pisitools.insinto("/usr/share/doc/%s/manual" % get.srcNAME(), "docs/gnuplot.pdf")
    #pisitools.insinto("/usr/share/doc/%s/tutorial" % get.srcNAME(), "tutorial/*.pdf")

    pisitools.dodoc("BUGS", "ChangeLog", "FAQ.pdf", "NEWS", "README*")
