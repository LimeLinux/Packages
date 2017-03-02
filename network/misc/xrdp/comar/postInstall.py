#!/usr/bin/python

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    os.system("xrdp-keygen xrdp /etc/xrdp/rsakeys.ini")

def preRemove():
    if os.path.exists("/etc/xrdp/rsakeys.ini"):
	os.system("rm /etc/xrdp/rsakeys.ini")
    

    
    

