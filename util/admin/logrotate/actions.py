#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\" WITH_ACL=yes" % get.CFLAGS())

def install():
    autotools.install()

    pisitools.dodir("/etc/logrotate.d")

    pisitools.dobin("examples/logrotate.cron", "/etc/cron.daily")
    pisitools.insinto("/etc", "examples/logrotate-default", "logrotate.conf")

    pisitools.dodoc("COPYING", "README*", "ChangeLog.md")
