
#!/usr/bin/python

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("rc-update add opentmpfiles-dev boot")
    os.system("rc-update add opentmpfiles-setup boot")

    os.system("rc-service add opentmpfiles-dev start")
    os.system("rc-service add opentmpfiles-setup start")
    

