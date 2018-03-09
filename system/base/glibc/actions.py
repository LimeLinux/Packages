#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 LimeLinux
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "glibc-2.27"

defaultflags = "-O3 -g -U_FORTIFY_SOURCE -fno-strict-aliasing -fomit-frame-pointer -mno-tls-direct-seg-refs"

multibuild = (get.ARCH() == "x86_64")
pkgworkdir = "%s/%s" % (get.workDIR(), WorkDir)

config = {"system": {
                "multi": False,
                "extraconfig": "--build=%s" % get.HOST(),
                "coreflags":   "",
                "libdir":      "lib",
                "libexecdir":  "/usr/lib/misc",
                "buildflags":  "%s" % (defaultflags),
                "builddir":    "%s/build" % pkgworkdir
            }
}



def set_variables(cfg):
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")
    shelltools.export("CC", "gcc %s" % cfg["coreflags"])
    shelltools.export("CXX", "g++ %s" % cfg["coreflags"])

    shelltools.export("CFLAGS", cfg["buildflags"])
    shelltools.export("CXXFLAGS", cfg["buildflags"])


### functionize repetetive tasks ###
def libcSetup(cfg):
    set_variables(cfg)

    if not os.path.exists(cfg["builddir"]):
        shelltools.makedirs(cfg["builddir"])

    shelltools.cd(cfg["builddir"])
    shelltools.system("../configure \
                       --with-tls \
                       --with-__thread \
                       --enable-add-ons=nptl,libidn \
                       --enable-stack-protector=strong \
                       --enable-bind-now \
                       --enable-obsolete-nsl \
                       --enable-obsolete-rpc \
                       --enable-kernel=3.2.0 \
                       --with-bugurl=https://bugs.limelinux.com/ \
                       --enable-stackguard-randomization \
                       --without-selinux \
                       --disable-profile \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       %s " % cfg["extraconfig"])

def libcBuild(cfg):
    set_variables(cfg)

    shelltools.cd(cfg["builddir"])

    autotools.make()

def libcInstall(cfg):
    # not to bork locale/zone stuff
    set_variables(cfg)

    # install glibc/glibc-locale files
    shelltools.cd(cfg["builddir"])
    autotools.rawInstall("install_root=%s" % get.installDIR())



### real actions start here ###
def setup():
    libcSetup(config["system"])


def build():
    libcBuild(config["system"])
    shelltools.echo("configparms", "slibdir=/usr/lib")
    shelltools.echo("configparms", "rtlddir=/usr/lib")
    shelltools.echo("configparms", "libdir=/usr/lib")



def install():
    libcInstall(config["system"])


    # localedata can be shared between archs
    shelltools.cd(config["system"]["builddir"])
    autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

    # now we do generic stuff
    shelltools.cd(pkgworkdir)

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")


    pisitools.insinto("/etc", "nscd/nscd.conf")
    
    pisitools.insinto("/usr/lib/tmpfiles.d", "nscd/nscd.tmpfiles", "nscd.conf")
    pisitools.insinto("/etc", "posix/gai.conf")
    
    pisitools.insinto("/etc", "locale.gen")
    shelltools.system("sed -e '1,3d' -e 's|/| |g' -e 's|\\\| |g' -e 's|^|#|g' %s/%s/localedata/SUPPORTED >> %s/etc/locale.gen" % (get.workDIR(),get.srcDIR(),get.installDIR()))
    
    #xlocale.h: No such file or directory
    pisitools.dosym("/usr/include/bits/locale.h", "/usr/include/xlocale.h")


    pisitools.dodoc("ChangeLog", "COPYING", "COPYING.LIB", "NEWS", "README*", "LICENSES")

