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
    #pisitools.cflags.add('-fpie -DSYSLOGD_PIDNAME=\\"syslogd.pid\\"')
  #  pisitools.ldflags.add("-pie -Wl,-z,relro -Wl,-z,now")
    shelltools.system("sed -i rsyslog.service.in \
    -e 's|rsyslogd -n|rsyslogd -n -i /run/rsyslogd.pid|' \
    -e '/ExecStart=.*$/iPIDFile=/run/rsyslogd.pid'")
    autotools.rawConfigure("\
                         --sbindir=/usr/bin \
                         --prefix=/usr  \
                         --disable-mysql \
                         --disable-pgsql \
                         --disable-relp \
                         --disable-gnutls \
                         --disable-static \
                         --disable-rfc3195 \
                         --disable-omjournal \
                         --disable-testbench \
                         --disable-mmnormalize \
                         --disable-gssapi-krb5 \
                         --disable-generate-man-pages \
                         --disable-uuid \
                         --enable-mail \
                         --enable-imdiag \
                         --enable-imfile \
                         --enable-imptcp \
                         --enable-mmanon \
                         --enable-omprog \
                         --enable-mmaudit \
                         --enable-pmsnare \
                         --enable-impstats \
                         --enable-omstdout \
                         --enable-omuxsock \
                         --enable-largefile \
                         --enable-pmlastmsg \
                         --enable-mmjsonparse \
                         --enable-pmcisconames \
			  --with-systemdsystemunitdir=no \
                         --enable-unlimited-select \
                         --enable-pmaixforwardedfrom")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README", "AUTHORS", "ChangeLog")
    
    # create needed directory
    pisitools.dodir("/var/spool/rsyslog")
    pisitools.dodir("/var/empty/dev")
