#!/usr/bin/python

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools


def build():
    pythonmodules.compile()
    pythonmodules.compile(pyVer = "3")


def install():
    pythonmodules.install()
    pythonmodules.install(pyVer = "3")

    pisitools.dodoc("ChangeLog", "COPYING")
