#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def setup():
    shelltools.echo("src/feature.h", "#define SYS_VIMRC_FILE \"/etc/vim/vimrc\"")


    options ="--with-features=huge \
              --enable-multibyte \
              --enable-perlinterp \
              --enable-pythoninterp \
              --enable-rubyinterp \
              --enable-gui=no \
              --with-tlib=ncurses \
              --prefix=/usr \
              --localstatedir=/var/lib/vim \
              --with-features=big \
              --disable-acl \
              --with-compiledby=limelinux \
              --enable-gpm \
              --enable-acl \
              --enable-cscope \
              --disable-netbeans \
              --enable-perlinterp \
              --disable-luainterp \
              --with-x=no \
              --with-modified-by=limelinux"

    if get.buildTYPE() == "gui":
        options += " --enable-gui=gtk2 \
                     --with-vim-name=gvim \
                     --with-view-name=gview \
                     --with-x=yes"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("VIMRCLOC=/etc/vim DESTDIR=%s" % get.installDIR())

    # enough for gui building, quit here
    if get.buildTYPE() == "gui":
        return

    # Vi != Vim, it's hard to break habbits
    pisitools.dosym("vim", "/usr/bin/vi")
    pisitools.dosym("/usr/bin/vim", "/bin/ex")

