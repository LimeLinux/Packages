#!/usr/bin/env python
#-*- coding:utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/__package_name__/work/ and:
# WorkDir="__package_name__-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    autotools.rawConfigure("--prefix=/usr")

def build():
    autotools.make("-j1")

def install():
    pisitools.dodoc("COPYING","INSTALL")
    autotools.rawInstall("DESTDIR=%s"%get.installDIR())
