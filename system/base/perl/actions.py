#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial=["perl"]

def setup():
    # use system zlib
    shelltools.unlinkDir("cpan/Compress-Raw-Zlib/zlib-src")
    pisitools.dosed("MANIFEST", "zlib-src", deleteLine=True)
    pisitools.dosed("cpan/Compress-Raw-Zlib/config.in", "(BUILD_ZLIB\s+=\s)True", r"\1False")
    pisitools.dosed("cpan/Compress-Raw-Zlib/config.in", "(INCLUDE\s+=\s)\.\/zlib-src", r"\1/usr/include")
    pisitools.dosed("cpan/Compress-Raw-Zlib/config.in", "(LIB\s+=\s)\.\/zlib-src", r"\1/usr/lib")

    shelltools.export("LC_ALL", "C")


    shelltools.system('sh Configure -des \
                      -Darchname=%s-linux \
                      -Dcccdlflags=-fPIC \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize="%s" \
                      -Duselargefiles \
                      -Dusethreads \
                      -Duseithreads \
                      -Dd_semctl_semun \
                      -Dscriptdir=/usr/bin \
                      -Dman1dir=/usr/share/man/man1 \
                      -Dman3dir=/usr/share/man/man3 \
                      -Dinstallman1dir=%s/usr/share/man/man1 \
                      -Dinstallman3dir=%s/usr/share/man/man3 \
                      -Dlibperl=libperl.so.%s \
                      -Duseshrplib \
                      -Dman1ext=1 \
                      -Dman3ext=3pm \
                      -Dcf_by="limelinux" \
                      -Ud_csh \
                      -Di_ndbm \
                      -Di_gdbm \
                      -Di_db \
                      -Ubincompat5005 \
                      -Uversiononly \
                      -Dpager="/usr/bin/less -isr" \
                      -Dlibpth="/lib /usr/lib" \
                      ' %(get.ARCH(), get.CC(), get.CFLAGS(), get.installDIR(), get.installDIR(), get.srcVERSION()))

def build():
    # colorgcc uses Term::ANSIColor
    paths = get.ENV("PATH").split(":")
    if "/usr/share/colorgcc" in paths:
        paths.remove("/usr/share/colorgcc")
    shelltools.export("PATH", ":".join(paths))
    ##
    autotools.make()



def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/perl")


    pisitools.dosym("/usr/bin/perl%s" % get.srcVERSION(), "/usr/bin/perl")

    # Perl5 library
    # NEEDS MODIFICATION FOR NEW VERSION
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so")
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5")
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.24")
    pisitools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.24.0")

    # Docs
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    shelltools.system('LD_LIBRARY_PATH=%s ./perl installhtml \
                       --podroot="." \
                       --podpath="lib:ext:pod:vms" \
                       --recurse \
                       --htmldir="%s/usr/share/doc/%s/html"' % (get.curDIR(), get.installDIR(), get.srcNAME()))

    pisitools.dodoc("Changes*", "Artistic", "Copying", "README", "AUTHORS")
