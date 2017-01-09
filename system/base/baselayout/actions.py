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
    pisitools.removeDir("/lib") 
    pisitools.dosym("usr/lib", "lib")
    pisitools.dodir("/usr/share/locale")
    pisitools.dodir("/usr/lib/locale")


    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        pisitools.dosym("usr/lib", "lib64")   
        pisitools.dosym("lib", "usr/lib64") 

        pisitools.dodir("/lib32")
        pisitools.dodir("/usr/lib32")


    pisitools.dosym("limelinux-release", "/etc/system-release")

    shelltools.touch("hostname")

    if get.ARCH() == "x86_64":
        shelltools.echo("hostname", "Limelinux")

    elif get.ARCH() == 'armv7h':
        shelltools.echo("hostname", "LimeArm")

    pisitools.insinto("/etc", "hostname")
    pisitools.remove("/etc/inittab")




