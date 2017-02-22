#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk/jre")

def build():    
    shelltools.system("ant -Dxbean.jar=xmlbeans-2.6.0/lib/xbean.jar -Djsr173.jar=xmlbeans-2.6.0/lib/jsr173_1.0_api.jar jar javadoc")

def install():
    pisitools.dobin("rhino")
    pisitools.dobin("rhino-jsc")
    pisitools.dobin("rhino-debugger")
    pisitools.doman("rhino.1")
    pisitools.doman("rhino-jsc.1")
    pisitools.doman("rhino-debugger.1")
    pisitools.insinto("/usr/share/java", "build/rhino1.7.7.1/js.jar")
    pisitools.insinto("/usr/share/java", "build/rhino1.7.7.1/js.jar", "js-1.7.7.1.jar")
