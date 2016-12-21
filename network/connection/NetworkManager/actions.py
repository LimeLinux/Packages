#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    # /var/run => /run
  #  for f in ["configure.ac", "src/Makefile.am", "src/Makefile.in"]:
   #     pisitools.dosed(f, "\$\(?localstatedir\)?(\/run\/(\$PACKAGE|NetworkManager))", "\\1")
    #pisitools.dosed("configure.ac", "\/var(\/run\/ConsoleKit)", "\\1")
    #pisitools.dosed("configure.ac", "^initscript", deleteLine=True)
    autotools.autoreconf("-fi")
    shelltools.system("intltoolize --force --copy --automake")

    autotools.configure("--disable-static \
                         --disable-silent-rules \
                         --disable-wimax \
                         --disable-lto \
                         --disable-config-plugin-ibft \
                         --disable-ifnet \
                         --disable-more-warnings \
                         --enable-modify-system \
                         --enable-concheck \
                         --without-netconfig \
                         --with-libsoup=yes \
                         --with-session-tracking=consolekit \
                         --with-suspend-resume=upower \
                         --with-system-ca-path=/etc/ssl/certs \
                         --with-crypto=nss \
                         --with-dhcpcd=/sbin/dhcpcd \
                         --with-dbus-sys-dir=/etc/dbus-1/system.d \
                         --with-dhclient=/usr/sbin/dhclient \
                         --with-kernel-firmware-dir=/lib/firmware \
                         --with-resolvconf=/etc/resolv.default.conf \
                         --with-iptables=/usr/sbin/iptables \
                         --with-dnsmasq=/usr/sbin/dnsmasq \
                         --with-nmtui \
                         --disable-ppp \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/NetworkManager \
                        ")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/var")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING", "COPYING", "NEWS", "README")
