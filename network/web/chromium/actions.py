#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "chromium-%s" % get.srcVERSION()

shelltools.export("HOME", get.workDIR())

ARCH = "x64"

def setup():
    shelltools.export("LC_ALL", "C")

    for LIB in ["flac", "harfbuzz-ng" "libwebp" ,"libxslt", "yasm"]:
        shelltools.system('find -type f -path "*third_party/$LIB/*" \! -path "*third_party/$LIB/chromium/*" \! -path "*third_party/$LIB/google/*" \! -regex ".*\.\(gn\|gni\|isolate\|py\)" -delete')

    shelltools.system("build/linux/unbundle/replace_gn_files.py --system-libraries flac harfbuzz-ng libwebp libxslt yasm")

    opt = 'use_sysroot=false \
           is_clang=false enable_nacl=false \
           enable_nacl_nonsfi=false \
           fieldtrial_testing_like_official_build=true \
           clang_use_chrome_plugins=false \
           symbol_level=0 \
           fatal_linker_warnings=false \
           treat_warnings_as_errors=false \
           use_cups=true \
           use_gnome_keyring=false\
           use_gold=false \
           use_kerberos=true \
           enable_hangout_services_extension=true \
           use_gconf=false \
           enable_widevine=true \
           linux_use_bundled_binutils=false \
           is_debug=false \
           ffmpeg_branding="Chrome" \
           google_default_client_secret="0ZChLK6AxeA3Isu96MkwqDR4" \
           google_api_key="AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM" \
           google_default_client_id="413772536636.apps.googleusercontent.com" \
           remove_webcore_debug_symbols=true \
           proprietary_codecs=true \
           link_pulseaudio=true \
           use_pulseaudio=true \
           use_gtk3=false'

    shelltools.system("tools/gn/bootstrap/bootstrap.py --gn-gen-args '%s'"% opt)
    shelltools.system("out/Release/gn gen out/Release --args='%s'"% opt)


def build():
    #Sandbox for error must remain separate
    shelltools.system("ninja -C out/Release chrome")
    shelltools.system("ninja -C out/Release chrome_sandbox")
    shelltools.system("ninja -C out/Release chromedriver")
    shelltools.system("ninja -C out/Release widevinecdmadapter")

def install():
    shelltools.cd("out/Release")

    #should be checked should for the missing folder "out/Release"
    for vla in ["*.pak", "*.json", "chrome", "locales", "resources", "icudtl.dat", "mksnapshot", "chromedriver", "natives_blob.bin", "snapshot_blob.bin", "character_data_generator"]:
        pisitools.insinto("/usr/lib/chromium", "%s" % vla)

    pisitools.insinto("/usr/lib/chromium", "chrome_sandbox", "chrome-sandbox")
    pisitools.dosym("/usr/lib/chromium/chrome", "/usr/bin/chromium")
 
    shelltools.system("chmod -v 4755 %s/usr/lib/chromium/chrome-sandbox" %get.installDIR())

    pisitools.newman("chrome.1", "chromium.1")

    shelltools.cd("../..")
    for size in ["22", "24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium.png")

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium.png", "/usr/share/pixmaps/chromium.png")

    pisitools.dodoc("LICENSE")
