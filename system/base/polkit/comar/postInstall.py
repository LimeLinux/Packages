#!/usr/bin/python

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    os.system("getent group polkitd >/dev/null || groupadd -g 102 polkitd")
    os.system("getent passwd polkitd >/dev/null || useradd -c 'Policy Kit Daemon' -u 102 -g polkitd -d '/' -s /bin/false polkitd")
    os.system("passwd -l polkitd &>/dev/null")
    os.system("chown 102 /var/lib/polkit-1")
    os.system("chown 102 /etc/polkit-1/rules.d")
    os.system("chown 102 /usr/share/polkit-1/rules.d")
    
    

