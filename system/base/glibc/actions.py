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

WorkDir = "glibc-2.23"



ldconf32bit = """/lib32
/usr/lib32
"""

multilib = " --enable-multi-arch --enable-multilib" if get.ARCH() == "x86_64" else " --disable-multi-arch --disable-multilib"
arch = "x86-64" if get.ARCH() == "x86_64" and not get.buildTYPE() == "emul32" else "i686"
defaultflags = "-O3 -g " 
if get.ARCH() == "x86_64": defaultflags += " -fasynchronous-unwind-tables -mtune=generic -march=%s" % arch
#if get.ARCH() == "armv7h": defaultflags += " --U_FORTIFY_SOURCE -march=armv7-a -mfloat-abi=hard -mfpu=vfpv3-d16"
if get.buildTYPE() == "emul32": defaultflags += " -m32"  



def setup():
    
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")
    
    if get.ARCH() == "x86_64" or get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc %s " % defaultflags)
        shelltools.export("CXX", "g++ %s " % defaultflags)

        shelltools.export("CFLAGS", defaultflags)
        shelltools.export("CXXFLAGS", defaultflags)
        
    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "--prefix=/usr \
               --libdir=/usr/lib \
               --mandir=/usr/share/man \
               --infodir=/usr/share/info \
               --libexecdir=/usr/lib/misc \
               --enable-add-ons \
               --enable-bind-now \
               --enable-kernel=2.6.32 \
               --enable-stackguard-randomization \
               --disable-profile \
                --disable-werror  \
               --enable-obsolete-rpc \
               --enable-lock-elision \
               %s \
               --with-tls"% multilib
               
    if get.buildTYPE() == "emul32":
        options += "\
                    --libdir=/usr/lib32 \
                    i686-pc-linux-gnu \
                   "

    shelltools.system("../configure %s" % options)

def build():
    shelltools.cd("build")
    if get.buildTYPE() == "emul32":
        shelltools.echo("configparms","build-programs=no")
        shelltools.echo("configparms", "slibdir=/lib32")
        shelltools.echo("configparms", "rtlddir=/lib32")
        shelltools.echo("configparms", "bindir=/tmp32")
        shelltools.echo("configparms", "sbindir=/tmp32")
        shelltools.echo("configparms", "rootsbindir=/tmp32")
        shelltools.echo("configparms", "datarootdir=/tmp32/share")

        autotools.make()

        pisitools.dosed("configparms", "=no", "=yes")

    else:
        shelltools.echo("configparms", "slibdir=/usr/lib")
        shelltools.echo("configparms", "rtlddir=/usr/lib")

    autotools.make()



def install():

    shelltools.cd("build")
    pisitools.dodir("/etc/ld.so.conf.d")
    shelltools.touch("%s/etc/ld.so.conf" % get.installDIR())


    autotools.rawInstall("install_root=%s" % get.installDIR())
    

    if get.buildTYPE() == "emul32":
        pisitools.dosym("/lib32/ld-linux.so.2", "/lib/ld-linux.so.2")

        shelltools.echo("%s/etc/ld.so.conf.d/60-glibc-32bit.conf" % get.installDIR(), ldconf32bit)


        pisitools.removeDir("/tmp32")




    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    # remove zoneinfo files since they are coming from timezone packages
    # we disable timezone build with a patch, keeping these lines for easier maintenance
    if shelltools.isDirectory("%s/usr/share/zoneinfo" % get.installDIR()):
        pisitools.removeDir("/usr/share/zoneinfo")

 
    shelltools.cd("..")
   
    
    pisitools.insinto("/etc", "nscd/nscd.conf")
    
    pisitools.insinto("/usr/lib/tmpfiles.d", "nscd/nscd.tmpfiles", "nscd.conf")
    pisitools.insinto("/etc", "posix/gai.conf")
    
    pisitools.insinto("/etc", "locale.gen")
    shelltools.system("sed -e '1,3d' -e 's|/| |g' -e 's|\\\| |g' -e 's|^|#|g' %s/%s/localedata/SUPPORTED >> %s/etc/locale.gen" % (get.workDIR(),get.srcDIR(),get.installDIR()))
      
 
    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "NAMESPACE", "NEWS", "PROJECTS", "README*", "LICENSES")

    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        pisitools.remove("/etc/ld.so.cache")

    pisitools.remove("/etc/ld.so.conf")


