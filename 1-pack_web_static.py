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

    a_nme = "web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))

    result = local("tar -cvzf versions/{} web_static".format(a_nme))

    if result.succeeded:
        return os.path.join("versions", a_nme)
    else:
        return None
