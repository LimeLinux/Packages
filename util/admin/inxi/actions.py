#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.dosed("inxi", "os-release", "limelinux-release")
    pisitools.dosed("inxi", "lackware-version SuSE-release", "lackware-version SuSE-release limelinux-release")
    pisitools.dobin("inxi")
    pisitools.doman("inxi.1.gz")
    pisitools.dodoc("inxi.changelog")
    
    pisitools.dosym("/usr/bin/inxi", "/usr/share/kde4/apps/konversation/scripts/inxi")
