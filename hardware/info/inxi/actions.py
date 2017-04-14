#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."

def install():   
    pisitools.insinto("/usr/bin/", "inxi")        
    pisitools.insinto("/usr/share/man/man1/", "inxi.1.gz") 


    pisitools.dodoc("inxi.changelog", "README.txt", "LICENSE.txt")  
    
    
