from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive name
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Create the .tgz archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    # Return the archive path if generated successfully, otherwise return None
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None
