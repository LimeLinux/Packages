#!/usr/bin/python

import os, re

OUR_ID = 445
OUR_NAME = "vnstat"
OUR_DESC = "VNSTAT"


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    try:
        os.system ("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/vnstat -r -s /bin/false -u %d -g %d %s -c %s" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
        os.system("mkdir /var/lib/vnstat")
        os.system("chown -R vnstat:vnstat /var/lib/vnstat")
    except:
        pass

def postRemove():
    try:
        os.system ("userdel %s" % OUR_NAME)
        os.system ("groupdel %s" % OUR_NAME)
    except:
        pass 
