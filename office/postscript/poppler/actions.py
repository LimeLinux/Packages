#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    options = "--disable-static \
               --disable-poppler-qt \
               --disable-gtk-doc-html \
               --disable-zlib \
               --disable-gtk-test \
               --enable-cairo-output \
               --enable-xpdf-headers \
               --enable-libjpeg \
               --enable-libopenjpeg"

    pisitools.cxxflags.add(" -std=c++11")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
