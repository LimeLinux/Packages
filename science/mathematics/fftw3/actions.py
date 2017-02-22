#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="fftw-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")

    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-double" % get.srcVERSION())
    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-long-double" % get.srcVERSION())
    shelltools.copytree("../fftw-%s" % get.srcVERSION(), "../fftw-%s-quad" % get.srcVERSION())
	
    options ="--enable-fortran \
		--prefix=/usr \
	        --enable-shared \
	        --disable-static \
                --disable-dependency-tracking \
                --enable-threads"
		  			 
    if get.ARCH() == "x86_64":

	options += " --enable-sse \
		    --enable-single"
    
    autotools.configure(options)
    
    shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    
    options1 ="\
                         --enable-shared \
                         --disable-static \
			 --enable-fortran \
                         --disable-dependency-tracking \
                         --enable-threads"
   
    if get.ARCH() == "x86_64":

	options1 += "--enable-quad-precision"
		    
		    			 
    autotools.configure(options1)

    # The only difference here is that there is no --enable-float
    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    
    options2 ="\
                         --enable-shared \
                         --disable-static \
			 --enable-fortran \
                         --disable-dependency-tracking \
                         --enable-threads"
			 
    if get.ARCH() == "x86_64":

	options2 += " --enable-sse2" 			 
    
    autotools.configure(options2)

    # The only difference here is --enable-long-double
    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    
    options3 ="--enable-shared \
                         --disable-static \
                         --disable-dependency-tracking \
                         --enable-threads \
                         --enable-fortran \
                         --enable-long-double"   
			 
	  
    
    autotools.configure(options3)


def build():
    autotools.make()

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.make()

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.make()

    shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-double" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-long-double" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s-quad" % get.srcVERSION())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../fftw-%s" % get.srcVERSION())

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO", "CONVENTIONS")
