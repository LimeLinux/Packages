#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 LimeLinux
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

ZoneDir = "/usr/share/zoneinfo"
TargetDir = "%s/%s" % (get.installDIR(), ZoneDir)

RightDir = "%s/right" % TargetDir
PosixDir = "%s/posix" % TargetDir

WorkDir = "tz-2018c"

Components = ["etcetera", "southamerica", "northamerica", "europe", "africa", "antarctica", \
              "asia", "australasia", "backward", "pacificnew",\
              "systemv" ]

ExtraDist = ["zone1970.tab", "zone.tab", "iso3166.tab"]

def setup():
    pisitools.dodir (ZoneDir)
    pisitools.dodir (RightDir)
    pisitools.dodir (PosixDir)


def install():
    for extra in ExtraDist:
        pisitools.insinto (ZoneDir, extra)

    for tz in Components:
        cmd = "zic  /dev/null -d %s -y \"%s/yearistype.sh\" %s" % (TargetDir, get.workDIR(), tz)
        shelltools.system (cmd)
        part2 = "zic  /dev/null -d %s -y \"%s/yearistype.sh\" %s" % (PosixDir, get.workDIR(), tz)
        shelltools.system (part2)
        part3 = "zic -L leapseconds -d %s -y \"%s/yearistype.sh\" " % (RightDir, get.workDIR())
        shelltools.system (part3)

    # Default DST
    shelltools.system ("zic  -d %s -p America/New_York" % TargetDir)
