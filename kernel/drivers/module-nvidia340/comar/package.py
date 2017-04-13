#!/usr/bin/python

import os


driver_dir_name = "nvidia340"
libdir = "/usr/lib/%s" % driver_dir_name
datadir = "/usr/share/%s" % driver_dir_name

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system(" /usr/sbin/alternatives \
                --install   /usr/lib/libGL.so.1.2.0                 libGL                   %(libdir)s/libGL.so.1.2.0     50 \
                --slave     /usr/lib/xorg/modules/volatile          xorg-modules-volatile   %(libdir)s/modules"
                % {"libdir": libdir, "datadir": datadir})


    # If this driver is in use, refresh links after installation.
    if os.readlink("/etc/alternatives/libGL") == "%s/libGL.so.1.2.0" % libdir:
        os.system("/usr/sbin/alternatives --set libGL %s/libGL.so.1.2.0" % libdir)
        os.system("/sbin/ldconfig -X")

        
def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("rc-update add nvidia-persistenced default")
    os.system("rc-update add nvidia-smi default")
    os.system("/usr/bin/nvidia-smi > /dev/null")
    os.system("Xorg :1 -configure")
    os.system("cp /root/xorg.conf.new /etc/X11/xorg.conf")



def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2.0" % libdir)
    pass
