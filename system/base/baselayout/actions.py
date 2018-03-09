# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    def chmod(path, mode):
        shelltools.chmod("%s%s" % (get.installDIR(), path), mode)

    # Install everything
    pisitools.insinto("/", "root/*")


    # Adjust permissions
    chmod("/tmp", 01777)
    chmod("/var/tmp", 01777)
    chmod("/run/shm", 01777)
    chmod("/var/lock", 0775)
    chmod("/usr/share/baselayout/shadow", 0600)

    # /usr/lib migration
    pisitools.dosym("usr/lib", "lib")
    pisitools.dodir("/usr/share/locale")
    pisitools.dodir("/usr/lib/locale")
    pisitools.dosym("usr/lib", "lib64")   
    pisitools.dosym("lib", "usr/lib64") 



    pisitools.dosym("limelinux-release", "/etc/system-release")

    shelltools.touch("hostname")

    shelltools.echo("hostname", "Limelinux")


    pisitools.insinto("/etc", "hostname")




