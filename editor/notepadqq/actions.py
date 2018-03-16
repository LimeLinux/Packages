#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="notepadqq-continuous"

def setup():
    #shelltools.move("../CodeMirror-5.33.0/*", "%s/src/editor/libs/codemirror" % get.workDIR())
    autotools.configure("--prefix /usr --qmake /usr/bin/qmake --lrelease /usr/bin/lrelease")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
