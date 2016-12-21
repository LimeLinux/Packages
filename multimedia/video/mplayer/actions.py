#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def setup():
    shelltools.copytree("../ffmpeg-3.0.2", "ffmpeg")
    autotools.rawConfigure("--prefix=/usr \
                            --disable-arts \
                            --disable-speex \
                            --disable-esd \
                            --disable-musepack \
                            --confdir=/etc/mplayer \
                            --disable-libdv \
                            --disable-ffmpeg_a")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    # install docs, tools, examples
    pisitools.dodoc("AUTHORS", "Changelog", "README", "LICENSE")
