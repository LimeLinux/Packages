#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # write layout's config
    os.system("chmod o+r /usr/lib/python2.7/site-packages/httplib2-0.8-py2.7.egg-info/top_level.txt")
