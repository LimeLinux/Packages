# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():

    options = '--with-audio="alsa oss"\
                --enable-int-quality'


    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README", "AUTHORS")

    pisitools.remove("/usr/lib/libmpg123.la")
