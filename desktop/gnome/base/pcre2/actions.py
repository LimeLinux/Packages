#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
   # autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
			    --enable-pcre2-16 \
			    --enable-pcre2-32 \
			    --enable-jit \
			    --enable-pcre2grep-libz \
			    --enable-pcre2grep-libbz2 \
			    --enable-pcre2test-libreadline  \
                         --docdir=/%s/%s \
                         --disable-static" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
