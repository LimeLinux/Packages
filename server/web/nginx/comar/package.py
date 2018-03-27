#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R nginx:nginx /var/lib/nginx")
    os.system("/bin/chown -R nginx:nginx /var/log/nginx")
    os.system("rc-update add nginx default")



def preRemove():
    # FIXME OpenRC service should also be deleted when package is deleted
    os.system("rc-update delete nginx default")
    pass

