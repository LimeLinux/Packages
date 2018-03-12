
#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # write layout's config
    os.system("rc-update add elogind boot")
    os.system("sysctl --system")
    os.system("sysctl kernel.sysrq=1")
    os.system('echo "1" > /proc/sys/kernel/sysrq')
