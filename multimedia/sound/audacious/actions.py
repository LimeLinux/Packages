#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dodoc("AUTHORS","COPYING","INSTALL")
    autotools.rawInstall("DESTDIR=%s"%get.installDIR())
