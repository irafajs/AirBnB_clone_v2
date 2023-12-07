#!/usr/bin/python3
"""
Shebang to make python script
"""


from fabric.api import env, put, run, local
from os.path import exists


env.hosts = ['100.25.134.107', '35.153.51.30']
env.user = 'ubuntu'
env.key_filename = '/home/vagrant/.ssh/school'


def do_deploy(archive_path):
    """Distrubute the archives to my server"""

    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        a_fnme = archive_path.split("/")[-1]
        release_folder = '/data/web_static/releases/' + a_fnme.split(".")[0]
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        run('rm -rf /tmp/{}'.format(archive_filename))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", e)
        return False


if __name__ == "__main__":
    archive_path = local('python 1-pack_web_static.py', capture=True)

    if archive_path:
        do_deploy(archive_path.strip())
    else:
        print("Error: Archive creation failed.")
