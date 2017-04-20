#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    #shelltools.system("sed -e '/Qt[CDN]/s/Qt/Qt5/g'")
    #shelltools.system("sed -e 's/moc_location/host_bins/'")
    shelltools.export("CXXFLAGS", "%s -fPIC -O2" % get.CXXFLAGS())
    autotools.autoreconf("-fi")
    shelltools.system("intltoolize --force --copy --automake")

    autotools.configure("--disable-static \
                         --enable-wifi \
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
                         --localstatedir=/var \
                         --with-libnm-glib \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/NetworkManager \
                         --with-kernel-firmware-dir=/usr/lib/firmware \
                         --with-dist-version='17.91-3, Lime Linux' \
                         --with-udev-dir=/usr/lib/udev \
                         --with-pppd=/usr/sbin/pppd \
                         --with-iptables=/sbin/iptables \
                        ")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/var")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING", "COPYING", "NEWS", "README")
