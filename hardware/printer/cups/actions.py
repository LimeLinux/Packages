#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():

    autotools.aclocal("-I config-scripts")
    autotools.autoconf("-I config-scripts")

    options = '--with-cups-user=lp \
               --with-cups-group=lp \
               --with-system-groups=lpadmin \
               --with-docdir=/usr/share/cups/html \
               --with-dbusdir=/etc/dbus-1 \
               --with-optim="%s" \
               --with-php=/usr/bin/php-cgi \
               --with-cupsd-file-perm=0755 \
               --with-log-file-perm=0600 \
               --without-java \
               --enable-acl \
               --enable-ssl=yes \
               --enable-libpaper \
               --enable-libusb=yes \
               --enable-debug \
               --enable-dbus \
               --enable-pam=yes \
               --enable-relro \
               --enable-dnssd \
               --enable-browsing \
               --enable-threads \
               --enable-raw-printing \
               --disable-gnutls \
               --disable-launchd \
               --without-rcdir \
               --libdir=/usr/lib \
               --without-perl \
               --with-logdir=/var/log/cups \
               --localstatedir=/var \
               --with-rundir=/run/cups \
               --with-xinetd=/etc/xinetd.d \
              ' % get.CFLAGS()


    autotools.configure(options)

def build():
    autotools.make()


def install():
    autotools.rawInstall("BUILDROOT=%s install-headers install-libs install-data install-exec" % get.installDIR())
    shelltools.chmod("%s/run/cups/certs" % get.installDIR(), 0755)

    pisitools.dodir("/usr/share/cups/profiles")

    # Serial backend needs to run as root
    #shelltools.chmod("%s/usr/lib/cups/backend/serial" % get.installDIR(), 0700)

    pisitools.dodoc("CHANGES.txt", "CREDITS.txt", "LICENSE.txt", "README.txt")
