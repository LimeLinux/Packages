# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
   # autotools.autoreconf("-vif")

# --enable-sysfs option provides better hardware information support with "lspci"
# --enable-32-bit option is not present anymore. Although build fails in emul32. With --disable-asm option, not fail. Needs to be tested.

    options ="\
              --with-dri-driverdir=/usr/lib/xorg/modules/dri \
              --with-egl-platforms=x11,drm,wayland \
              --with-vulkan-drivers=intel,radeon \
              --enable-xa \
              --enable-dri \
              --enable-egl \
              --enable-gbm \
              --enable-glx \
              --enable-dri3 \
              --enable-gles1 \
              --enable-gles2 \
              --enable-vdpau \
              --enable-osmesa \
              --enable-sysfs \
              --enable-xvmc \
              --enable-glx-tls \
              --enable-gallium-llvm \
              --enable-shared-glapi \
              --enable-texture-float \
             "
	     
    if get.buildTYPE() == "emul32":
        # compile with llvm doesn't work for now, test it later
        options += " --with-dri-driverdir=/usr/lib32/xorg/modules/dri \
                     --with-gallium-drivers=r600,nouveau,swrast \
                     --with-clang-libdir=/usr/lib32 \
                     --disable-gallium-llvm \
                     --disable-asm "

    elif get.ARCH() == "x86_64":

        options += " --with-clang-libdir=/usr/lib \
	                 --with-gallium-drivers=r300,r600,radeonsi,nouveau,svga,swrast,virgl \
	                 --with-dri-drivers=i915,i965,r200,radeon,nouveau,swrast \
		             --enable-nine \
		             --enable-llvm-shared-libs \
                     --enable-opencl-icd \
                     --enable-xa \
                     --enable-vdpau \
                     --enable-omx \
                     --enable-opencl \
                     --enable-opencl-icd \
                   "
    elif get.ARCH() == 'armv7h':

        options += " --with-dri-drivers=nouveau,swrast \
	             --with-gallium-drivers=nouveau,svga,swrast \
		   "
	
    autotools.configure(options)
    pisitools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.insinto("/usr/lib/mesa/", "%s/usr/lib/libGL.so.1.2.0"% get.installDIR())
    #pisitools.dosym("/usr/lib/mesa/libGL.so.1.2.0", "/usr/lib/libGL.so.1.2")

    #pisitools.domove("/usr/lib/libGLESv*", "/usr/lib/mesa/")
    #pisitools.domove("/usr/lib/libEGL*", "/usr/lib/mesa/")



    if get.buildTYPE() == "emul32":
        return

   # pisitools.dodoc("docs/COPYING")
    pisitools.dohtml("docs/*")


