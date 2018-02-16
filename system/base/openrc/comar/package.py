#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.popen("/sbin/telinit u &> /dev/null")
    os.system("rc-update add agetty.tty1 default")
    os.system("rc-update add agetty.tty2 default")
    os.system("rc-update add agetty.tty3 default")
    os.system("rc-update add agetty.tty4 default")
    os.system("rc-update add agetty.tty5 default")
    os.system("rc-update add agetty.tty6 default")

