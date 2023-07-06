#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
"""
from fabric.api import run, env, local
from os.path import exists

# Set the web server IP addresses
env.hosts = ['100.24.206.171', '54.173.234.218']


def do_clean(number=0):
    """Deletes out-of-date archives."""

    # Convert the number to an integer
    number = int(number)

    if number < 0:
        number = 0
    elif number == 1:
        number = 2

    try:
        # Get the list of archives in the versions folder
        archives = sorted(local('ls -1t versions', capture=True).split('\n'))

        # Delete the unnecessary archives in the versions folder
        for archive in archives[number:]:
            local('rm versions/{}'.format(archive))

        # Get the list of archives in the releases folder on the web servers
        releases = sorted(run('ls -1t /data/web_static/releases').split('\n'))

        # Delete the unnecessary archives in the releases folder on the web servers
        for release in releases[number:]:
            if release != 'test':
                run('rm -rf /data/web_static/releases/{}'.format(release))

        return True
    except Exception as e:
        print(str(e))
        return False
