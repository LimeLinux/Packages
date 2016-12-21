#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

    # Use secure delete. Even if the data is deleted with sqlite query, the traces of the deleted data still remains in the file
    # but cannot be seen with sqlite query. However, it can be seen by opening the file with a text editor.
    # SQLITE_SECURE_DELETE overwrites written data with zeros.
def setup():
    pisitools.cflags.add("-DSQLITE_SECURE_DELETE",
                         "-DSQLITE_ENABLE_UNLOCK_NOTIFY",
                         "-DSQLITE_ENABLE_COLUMN_METADATA",
                         "-DSQLITE_DISABLE_DIRSYNC",
                         "-DSQLITE_ENABLE_FTS3",
                         "-DSQLITE_ENABLE_FTS4",
                         "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
                         "-DSQLITE_ENABLE_STMT_SCANSTATUS",
			 "-DSQLITE_ENABLE_DBSTAT_VTAB=1",
                         "-DSQLITE_SOUNDEX",
                         "-DSQLITE_ENABLE_RTREE",
                         "-DSQLITE_ENABLE_API_ARMOR")

    pisitools.cflags.sub("-O[s\d]", "-O3")

    autotools.configure("--disable-static \
                         --enable-readline \
                         --enable-threadsafe")


def build():
    autotools.make("-j1")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())


    pisitools.dodoc("README*")

    shelltools.cd("%s/sqlite-doc-3130000" % get.workDIR())
    shelltools.system("pwd")

    pisitools.insinto("/usr/share/doc/sqlite", "../sqlite-doc-3130000/*")
   

