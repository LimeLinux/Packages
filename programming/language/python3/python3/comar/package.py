#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # write layout's config
    os.system("xrdb -load /dev/null")
    os.system("xrdb -query")


