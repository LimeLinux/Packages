#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R postgres:postgres /var/lib/postgres")
    os.system("/bin/chmod -R 0700 /var/lib/postgres/data")
    os.system("/bin/chmod -R 0700 /var/lib/postgres/backups")

    # On first install...
    if not os.path.exists("/var/lib/postgres/data/base"):
        for i in ["LANG", "LANGUAGE", "LC_ALL"]:
            os.environ[i] = "en_US.UTF-8"

        os.system('/bin/su postgres -s /bin/sh -p -c "/usr/bin/initdb --pgdata /var/lib/postgres/data"')