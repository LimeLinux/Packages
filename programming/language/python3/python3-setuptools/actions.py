# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="setuptools-%s" % get.srcVERSION()

def install():    
    pythonmodules.install(pyVer = "3")
    pisitools.rename("/usr/bin/easy_install", "py3easy-install")
    #avoid python-setuptools conflict
    pisitools.removeDir("/usr/share")
