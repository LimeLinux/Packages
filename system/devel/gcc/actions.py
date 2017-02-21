#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

snapshot = False

if snapshot:
    verMajor, verMinor = get.srcVERSION().replace("pre", "").split("_", 1)
    WorkDir = "gcc-4.7-%s" % verMinor
else:
    verMajor = get.srcVERSION()

arch = get.ARCH().replace("x86_64", "x86-64")

opt_arch = "--with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16" if get.ARCH() == "armv7h" else "--with-arch_32=i686"

opt_multilib = "--enable-multilib" if get.ARCH() == "x86_64" else "--disable-multilib"

# WARNING: even -fomit-frame-pointer may break the build, stack protector, fortify source etc. are off limits
cflags = "-O2 -g"




def exportFlags():
    # we set real flags with new configure settings, these are just safe optimizations
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cflags)
    shelltools.export("LDFLAGS", "")

    # FIXME: this may not be necessary for biarch
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")


def setup():
    exportFlags()
    pisitools.flags.remove("-pipe")
    # Maintainer mode off, do not force recreation of generated files
    #shelltools.system("contrib/gcc_update --touch")
    pisitools.dosed("gcc/Makefile.in", "\.\/fixinc\.sh", "-c true")
    pisitools.dosed("gcc/configure", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")
    pisitools.dosed("libiberty/configure", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")
    
    pisitools.dosed("gcc/config/i386/t-linux64", "^(ac_cpp='\$CPP\s\$CPPFLAGS)", r"\1 -O2")
    pisitools.system("sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64")
   

    shelltools.cd("../")
    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system('.././gcc-%s/configure \
                       --prefix=/usr \
                       --bindir=/usr/bin \
                       --libdir=/usr/lib \
                       --libexecdir=/usr/lib \
                       --includedir=/usr/include \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-bugurl=http://bugs.limelinux.com \
                       --enable-languages=c,c++,fortran,lto,objc,obj-c++ \
                       --disable-libgcj \
                       --enable-shared \
                       --enable-threads=posix \
                       --with-system-zlib \
                       --enable-__cxa_atexit \
                       --disable-libunwind-exceptions \
                       --enable-clocale=gnu \
                       --disable-libstdcxx-pch \
                       --disable-libssp \
                       --enable-gnu-unique-object \
                       --enable-linker-build-id \
                       --enable-cloog-backend=isl \
                       --disable-cloog-version-check \
                       --enable-lto \
                       --enable-plugin \
                       --with-linker-hash-style=gnu \
                       --with-pkgversion="Pisi Linux" \
                       --disable-werror \
                       --enable-checking=release \
                       --build=%s \
                               %s \
                               %s ' % ( verMajor , get.HOST(), opt_arch, opt_multilib))

def build():
    exportFlags()

    shelltools.cd("../build")
    autotools.make()

def install():
    shelltools.cd("../build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #autotools.install()

    for header in ["limits.h","syslimits.h"]:
        pisitools.insinto("/usr/lib/gcc/%s/%s/include" % (get.HOST(), verMajor) , "gcc/include-fixed/%s" % header)

    # Not needed
    pisitools.removeDir("/usr/lib/gcc/*/*/include-fixed")
    pisitools.removeDir("/usr/lib/gcc/*/*/install-tools")

    # This one comes with binutils
    #pisitools.remove("/usr/lib*/libiberty.a")

    # cc symlink
    pisitools.dosym("/usr/bin/gcc" , "/usr/bin/cc")

    # /lib/cpp symlink for legacy X11 stuff
    pisitools.dosym("/usr/bin/cpp", "/lib/cpp")


    # autoload gdb pretty printers
    gdbpy_dir = "/usr/share/gdb/auto-load/usr/lib/"
    pisitools.dodir(gdbpy_dir)

    gdbpy_files = shelltools.ls("%s/usr/lib/libstdc++*gdb.py*" % get.installDIR())
    for i in gdbpy_files:
        pisitools.domove("/usr/lib/%s" % shelltools.baseName(i), gdbpy_dir)


