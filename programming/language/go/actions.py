#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("GOROOT", "%s/go-go1.7.1" % get.workDIR())
shelltools.export("GOBIN", "$GOROOT/bin")
shelltools.export("GOPATH", "%s" % get.workDIR())
shelltools.export("GOROOT_FINAL", "/usr/lib/go")
shelltools.export("GOROOT_BOOTSTRAP", "/usr/bin/go")

shelltools.export("GOOS","linux")
shelltools.export("GOARCH","amd64")

NoStrip=["/"]

def build():
    shelltools.cd("src")
    shelltools.export("GOROOT", "%s/go-go1.7.1" % get.workDIR())
    shelltools.export("GOBIN", "$GOROOT/bin")
    shelltools.export("GOPATH", "%s" % get.workDIR())
    shelltools.export("GOROOT_FINAL", "/usr/lib/go")
    shelltools.export("GOROOT_BOOTSTRAP", "%s/go-go1.7.1/go-linux-amd64-bootstrap" % get.workDIR())

    shelltools.export("GOOS","linux")
    shelltools.export("GOARCH","amd64")
    shelltools.system("bash make.bash")

    shelltools.cd("%s/go-go1.7.1" % get.workDIR())



    for tool in ["godex", "godoc", "goimports", "gomvpkg", "gorename", "gotype"]:
        shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
        shelltools.system("$GOROOT/bin/go build -v -x -o $GOPATH/bin/%s golang.org/x/tools/cmd/%s" % (tool, tool))


    for tool in ["benchcmp" ,"bundle", "callgraph", "digraph", "eg", "fiximports", "guru", "html2article", "present", "ssadump", "stress", "stringer"]:
        shelltools.system("$GOROOT/bin/go get -d golang.org/x/tools/cmd/%s" % tool)
        shelltools.system("$GOROOT/bin/go build -v -x -o $GOROOT/pkg/tool/$GOOS\_$GOARCH/%s golang.org/x/tools/cmd/%s" % (tool, tool))


def install():  
    shelltools.cd("%s/go-go1.7.1" % get.workDIR())
    
    pisitools.dobin("bin/*")
    pisitools.dodir("/usr/lib/go")
    pisitools.insinto("/usr/share/doc/go", "doc")
  #  pisitools.insinto("/usr/lib/go", "include")
    pisitools.insinto("/usr/lib/go", "lib")
    pisitools.insinto("/usr/lib/go", "pkg")
    pisitools.insinto("/usr/lib/go", "src")
    
    pisitools.removeDir("/usr/lib/go/pkg/linux_amd64")
    
    pisitools.dodoc("VERSION", "LICENSE", "PATENTS", "README.*", "AUTHORS", "CONTRIBUTORS")
