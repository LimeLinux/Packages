#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools
import os
import shutil

# Avoid g-ir-scanner FTB/SV
shelltools.export ("HOME", get.installDIR())

# Circular deps  - woo
IgnoreAutodep = True

def setup():
    if get.buildTYPE() == "emul32":
        host = "--build=i686-pc-linux-gnu --host=i686-pc-linux-gnu"
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig:/usr/share/pkgconfig")
        shelltools.export("CFLAGS", "-I/usr/lib32/glib2/include " + get.CFLAGS() + " -fno-lto")
        autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/lib32 \
                            --disable-tests \
                            --disable-ima \
                            --disable-seccomp \
                            --enable-pam \
                            --disable-kmod \
                            --disable-networkd \
                            --enable-split-usr \
                            --disable-libiptc \
                            --disable-lz4 \
                            --disable-manpages \
                            --without-python \
                            --disable-selinux \
                            --enable-compat-libs \
                            --disable-myhostname \
                            --disable-libcurl \
                            --disable-libidn \
                            --disable-hostnamed \
                            --disable-libcryptsetup \
                            CFLAGS=\"$CFLAGS\"")
    else:
        autotools.configure ("--libexecdir=/usr/lib \
                          --localstatedir=/var  \
                          --sysconfdir=/etc \
                          --with-sysvinit-path=/etc/init.d \
                          --disable-networkd \
                          --disable-selinux \
                          --enable-compat-libs \
                          --with-pamlibdir=/lib/security \
                          --enable-split-usr \
                          --disable-terminal \
                          --enable-vconsole \
                          --disable-kdbus \
                          CFLAGS=\"%s -fno-lto\"" % get.CFLAGS())

def build():
    autotools.make ()

def install():
    idir = get.installDIR()
    # Force to subdirectory so we dont trash 64-bit installs
    if get.buildTYPE() == "emul32":
        idir += "/derpmcderp"

    autotools.rawInstall ("DESTDIR=%s" % idir)

    bdir = os.path.join(get.installDIR(), ".cache")
    if os.path.exists(bdir):
        shutil.rmtree(bdir)

    if get.buildTYPE() == "emul32":
        pisitools.dodir("/usr")
        shelltools.system("mv \"%s/usr/lib32\" \"%s/usr/.\"" % (idir, get.installDIR()))
        shutil.rmtree(idir)
        # udev compatibility stuff
        pisitools.dosym ("/usr/lib32/libudev.so", "/usr/lib32/libudev.so.0")
        return

   # udev compatibility stuff
    pisitools.dosym ("/usr/lib/libudev.so", "/usr/lib/libudev.so.0")

    pisitools.dosym ("/usr/bin/udevadm", "/sbin/udevadm")
    pisitools.dosym ("/usr/lib/systemd/systemd-udevd", "/lib/udev/udevd")

    # Final tweaks ^^
    pisitools.dosym ("/usr/lib/systemd/systemd", "/bin/systemd")


    #pisitools.dosym ("/usr/lib/systemd/systemd", "/sbin/init")

    # Make the journal directory
    pisitools.dodir ("/var/log/journal")

    # Install controll symlinks
    for control_item in ["reboot", "shutdown", "poweroff", "halt"]:
        pisitools.dosym ("/usr/bin/systemctl", "/sbin/%s" % control_item)


    pisitools.remove("/usr/include/gudev-1.0/gudev/gudevdevice.h")
    pisitools.remove("/usr/lib/pkgconfig/libudev.pc")
    pisitools.remove("/usr/lib/girepository-1.0/GUdev-1.0.typelib")
    pisitools.remove("/etc/udev/udev.conf")
    pisitools.remove("/usr/include/gudev-1.0/gudev/gudevenumerator.h")
    pisitools.remove("/usr/include/gudev-1.0/gudev/gudevenums.h")
    pisitools.remove("/sbin/halt")
    pisitools.remove("/sbin/reboot")
    pisitools.remove("/usr/share/man/man7/udev.7")
    pisitools.remove("/usr/include/gudev-1.0/gudev/gudevenumtypes.h")
    pisitools.remove("/usr/share/man/man5/udev.conf.5")
    pisitools.remove("/usr/include/libudev.h")
    pisitools.remove("/sbin/shutdown")
    pisitools.remove("/usr/lib/libudev.so")
    pisitools.remove("/usr/include/gudev-1.0/gudev/gudevclient.h")
    pisitools.remove("/sbin/udevadm")
    pisitools.remove("/usr/share/gir-1.0/GUdev-1.0.gir")
    pisitools.remove("/usr/share/man/man8/runlevel.8")
    pisitools.remove("/usr/lib/pkgconfig/gudev-1.0.pc")
    pisitools.remove("/usr/include/gudev-1.0/gudev/gudevtypes.h")
    pisitools.remove("/sbin/poweroff")
    pisitools.remove("/usr/include/gudev-1.0/gudev/gudev.h")
    pisitools.remove("/usr/lib/libgudev-1.0.so.0")
    pisitools.remove("/usr/share/man/man8/udevadm.8")
    pisitools.remove("/usr/share/man/man8/halt.8")
    pisitools.remove("/usr/lib/libgudev-1.0.so.0.2.0")
    pisitools.remove("/usr/share/man/man8/shutdown.8")

    pisitools.remove("/usr/share/man/man8/reboot.8")
    pisitools.remove("/usr/share/man/man8/poweroff.8")
    pisitools.remove("/usr/share/pkgconfig/udev.pc")
    pisitools.remove("/usr/share/man/man8/telinit.8")
    pisitools.remove("/usr/lib/libgudev-1.0.so")

    # Remove unwanted rpm macro
    pisitools.removeDir ("/usr/lib/rpm")



