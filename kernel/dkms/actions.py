#!/usr/bin/python

# Lime Linux 2017

from pisi.actionsapi import pisitools, autotools, get

def build():
    autotools.make ()

def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR()),
