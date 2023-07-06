#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
"""
from fabric.api import put, run, env
from os.path import exists

# Set the web server IP addresses
env.hosts = ['	100.24.206.17', '54.173.234.218']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""

    # Check if the archive file exists
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension
        archive_filename = archive_path.split('/')[-1].split('.')[0]

        # Create the release directory
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_filename))

        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(archive_filename, archive_filename))

        # Delete the archive from the web server
        run('rm /tmp/{}.tgz'.format(archive_filename))

        # Move the files from the web_static directory to the release directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'
            .format(archive_filename, archive_filename))

        # Remove the now empty web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_filename))

        return True
    except Exception as e:
        print(str(e))
        return False
