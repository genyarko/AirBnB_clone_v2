#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
"""
from fabric.api import run, put, env
from os.path import exists

# Set the web server IP addresses
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""

    # Check if the archive file exists
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Get the filename without extension
        archive_filename = archive_path.split('/')[-1]
        archive_filename_no_ext = archive_filename.split('.')[0]

        # Create the release directory
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_filename_no_ext))

        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, archive_filename_no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the files from the release directory to the parent directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_filename_no_ext, archive_filename_no_ext))

        # Remove the now empty web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_filename_no_ext))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_filename_no_ext))

        return True
    except:
        return False
