#!/usr/bin/python3
"""
Shebang to make python script
"""

from fabric.api import env, local
from os.path import isfile
from datetime import datetime
from fabric.operations import put, run
from fabric.context_managers import cd

env.hosts = ['100.25.134.107', '35.153.51.30']
env.user = 'ubuntu'
env.key_filename = '100.25.134.107', '35.153.51.30'

def do_pack():
    """method to archive all content of dir webstatic."""
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(current_time)
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception as e:
        print("Error during archive creation:", e)
        return None

def do_deploy(archive_path):
    """Distrubute the archives to my server."""
    if not isfile(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1].split('.')[0]
        release_folder = '/data/web_static/releases/{}'.format(archive_filename)

        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(archive_filename, release_folder))
        run('rm /tmp/{}.tgz'.format(archive_filename))

        current_link_path = '/data/web_static/current'
        if run('test -d {}'.format(current_link_path), warn_only=True).succeeded:
            run('rm -rf {}'.format(current_link_path))

        run('ln -s {} {}'.format(release_folder, current_link_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", e)
        return False

def deploy():
    """Calls do_pack() and do_deploy(archive_path) functions."""
    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False

if __name__ == "__main__":
    deploy()

