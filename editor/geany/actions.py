#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
	autotools.configure()
	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	pisitools.dodoc('AUTHORS', 'ChangeLog', 
	                'COPYING', 'HACKING', 'NEWS', 'README')
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

