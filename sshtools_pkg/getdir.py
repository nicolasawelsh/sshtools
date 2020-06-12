import os
import posixpath
from stat import S_ISDIR
from stat import S_ISREG


def getdir(sftp, remote_dir, local_dir, exclude=True, *file_extensions):
    # Recursively download dir from remote to local
    # argv: List of extensions to accept in download (will download all if left blank)
    # Example: getdir(sftp, "/mnt/example_dir", "C:/example_dir", ".dvl", ".mat")

    for item in sftp.listdir_attr(remote_dir):
        local_item = os.path.join(local_dir, item)
        remote_item = posixpath.join(remote_dir, item)
        if S_ISREG(item.st_mode):
            if file_extensions is None:
                sftp.get(remote_item, local_item)
            else:
                file_extension = os.path.splitext(local_item)[-1]
                if file_extension in file_extensions:
                    sftp.get(remote_item, local_item)
        elif S_ISDIR(item.st_mode):
            getdir(sftp, remote_item, local_item)
