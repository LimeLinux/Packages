#!/usr/bin/python

import os

driver_dir_name = "nvidia-current"
libdir = "/usr/lib/%s" % driver_dir_name
datadir = "/usr/share/%s" % driver_dir_name

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system(" /usr/sbin/alternatives \
                --install   /usr/lib/libGL.so.1.2.0                 libGL                   %(libdir)s/libGL.so.1.2.0     50 \
                --slave     /usr/lib/xorg/modules/volatile          xorg-modules-volatile   %(libdir)s/modules"
                % {"libdir": libdir, "datadir": datadir})
#                --slave     /etc/X11/XvMCConfig                     XvMCConfig              %(datadir)s/XvMCConfig \
#                --slave     /etc/ld.so.conf.d/10-nvidia.conf        nvidia-ldsoconf         %(datadir)s/ld.so.conf"
    

    # If this driver is in use, refresh links after installation.
    if os.readlink("/etc/alternatives/libGL") == "%s/libGL.so.1.2.0" % libdir:
        os.system("/usr/sbin/alternatives --set libGL %s/libGL.so.1.2.0" % libdir)
        os.system("/sbin/ldconfig -X")


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
        os.system("nvidia-xconfig")
        os.system("rc-update add nvidia-persistenced default")
        os.system("rc-update add nvidia-smi default")
        os.system("/usr/bin/nvidia-smi > /dev/null")
        

        


def preRemove():
    # FIXME OpenRC service should also be deleted when package is deleted
    os.system("rc-update delete nvidia-persistenced default")
    os.system("rc-update delete nvidia-smi default")
    pass
