#!/usr/bin/python

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("getent group 81 >/dev/null && userdel messagebus >/dev/null || true")
    os.system("getent group dbus >/dev/null || groupadd -g 81 dbus")
    os.system("getent passwd dbus >/dev/null || useradd -c 'System message bus' -u 81 -g dbus -d '/' -s /bin/false dbus")
    os.system("passwd -l dbus &>/dev/null")
    os.system("dbus-uuidgen --ensure")
    

