#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "")


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")	
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr      \
      -DCMAKE_BUILD_TYPE=Release       \
      -DENABLE_CXX11=ON                \
      -DBUILD_PERF_TESTS=OFF           \
      -DWITH_XINE=ON                   \
      -DBUILD_TESTS=OFF                \
      -DENABLE_PRECOMPILED_HEADERS=OFF \
      -DCMAKE_SKIP_RPATH=ON            \
      -DBUILD_WITH_DEBUG_INFO=OFF      \
      -Wno-dev", sourceDir="..")


def build():
    shelltools.cd("build")
    cmaketools.make("VERBOSE=1")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

