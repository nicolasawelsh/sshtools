import os
import posixpath
from stat import S_ISDIR
from stat import S_ISREG


def getdir(sftp, remote_dir, local_dir, *file_extensions, exclude=True):
    # Recursively download entire dir from remote to local

    # sftp:             SSH File Transfer Protocol (established with ssh.open_sftp())
    # remote_dir:       Remote dir to copy
    # local_dir:        Local  dir to paste
    # *file_extensions: File extensions to either be included or excluded from download
    # exclude:          If set to True,       listed file extensions will be excluded from the files to be downloaded
    #                   If set to False, ONLY listed file extensions will be included   in the files to be downloaded

    # Example call: getdir(sftp, "/remote/path", "/local/path", ".png", ".jpeg", exclude=False)

    for item in sftp.listdir_attr(remote_dir):
        local_item = os.path.join(local_dir, item)
        remote_item = posixpath.join(remote_dir, item)
        if S_ISREG(item.st_mode):
            if file_extensions is None:
                sftp.get(remote_item, local_item)
            else:  # Extensions specified
                file_extension = os.path.splitext(local_item)[-1]
                if exclude is False:
                    if file_extension in file_extensions:
                        sftp.get(remote_item, local_item)
                else:  # Exclude is True
                    if file_extension not in file_extensions:
                        sftp.get(remote_item, local_item)
        elif S_ISDIR(item.st_mode):
            os.mkdir(local_item)
            getdir(sftp, remote_item, local_item)
    return
