#!/usr/bin/python

import os
import glob

def createNode(mode, uid, gid, minor, major, path):
    os.system("/bin/mknod --mode=%d %s c %d %d" % (mode, path, minor, major))
    os.system("/bin/chown %s:%s %s" % (uid, gid, path))

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    createNode(600, "root", "root",     1, 11,      "/lib/udev/devices/kmsg")
    createNode(666, "root", "root",     1, 3,       "/lib/udev/devices/null")
    createNode(666, "root", "root",     1, 5,       "/lib/udev/devices/zero")
    createNode(600, "root", "root",     10, 130,    "/lib/udev/devices/watchdog")
    createNode(666, "root", "root",     10, 229,    "/lib/udev/devices/fuse")
    createNode(600, "root", "tty",      5, 1,       "/lib/udev/devices/console")
    createNode(666, "root", "tty",      5, 2,       "/lib/udev/devices/ptmx")
    createNode(666, "root", "tty",      5, 0,       "/lib/udev/devices/tty")
    createNode(620, "root", "tty",      4, 1,       "/lib/udev/devices/tty1")
    createNode(600, "root", "root",     10, 200,    "/lib/udev/devices/net/tun")
    createNode(600, "root", "root",     36, 0,      "/lib/udev/devices/route")
    createNode(600, "root", "root",     10, 200,    "/lib/udev/devices/skip")
    createNode(660, "root", "dialout",  108, 0,     "/lib/udev/devices/ppp")

    os.system("/sbin/udevadm hwdb --update")

    if os.path.exists("/lib/udev/devices/rtc"):
        os.unlink("/lib/udev/devices/rtc")

    # Migrate UDEV database
    if fromVersion and int(fromVersion) < 165:
        os.system("/sbin/udevadm info --convert-db &> /dev/null")


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # FIXME: All of these should be run only once during first install
    # but we can't do this in pisi, i think.

    # graphical.target is the default if xdm is enabled
    target = "/lib/systemd/system/graphical.target"

    # FIXME: We should clean this somewhere or else on every install of systemd
    # The default will get overriden by the old mudur service state
    # Maybe we can depend on the new mudur which will clean up around, or
    # mudur can be the one who creates this link
    #if os.path.exists("/etc/mudur/services/disabled/xdm"):
       # target = "/lib/systemd/system/multi-user.target"

    # set the default target if not set before
    if not os.path.islink("/etc/systemd/system/default.target"):
        os.symlink(target, "/etc/systemd/system/default.target")

    # Enable the services installed by default
    os.system("/bin/systemctl enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service")


# Fedora disables all services enabled in postInstall during preuninstall
# But do we really need this
#def preRemove():
#    os.system("/bin/systemctl disable \
#                getty@.service \
#                remote-fs.target \
#                systemd-readahead-replay.service \
#                systemd-readahead-collect.service")
#    try:
#       os.unlink("/etc/systemd/system/default.target")
#    except OSError:
#       pass
