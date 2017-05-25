#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 722 /home/ftp/incoming")
    os.system("/bin/chown ftp:ftp /home/ftp/incoming -R")
    os.system("rc-service vsftpd start")
    os.system("update-rc add vsftpd")
