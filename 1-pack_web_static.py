#!/usr/bin/python3
"""
Shebang to make python script
"""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """method to archive all content of dir webstatic"""

    local("mkdir -p versions")

    archive_name = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    result = local("tar -cvzf versions/{} web_static".format(archive_name), capture=True)

    if result.succeeded:
        return os.path.join("versions", archive_name)
    else:
        return None
