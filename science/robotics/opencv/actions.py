#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#shelltools.export("PYTHONDONTWRITEBYTECODE", "")


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")	
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DWITH_OPENCL=ON \
                          -DWITH_OPENGL=ON \
                          -DBUILD_EXAMPLES=ON \
                          -DINSTALL_C_EXAMPLES=ON \
                          -DINSTALL_PYTHON_EXAMPLES=ON \
                          -DCMAKE_BUILD_TYPE=Release       \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib  \
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
    cmaketools.make()

def install():
    pisitools.dodoc("CONTRIBUTING.md", "README.md", "LICENSE")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())



