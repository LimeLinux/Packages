#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import pythonmodules , pisitools

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog","README")
