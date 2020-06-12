import os
import posixpath


def putdir(sftp, local_dir, remote_dir, *file_extensions, exclude=True):
    # Recursively upload entire dir from local to remote

    # sftp:             SSH File Transfer Protocol (established with ssh.open_sftp())
    # local_dir:        Local  dir to copy
    # remote_dir:       Remote dir to paste
    # *file_extensions: File extensions to either be included or excluded from download
    # exclude:          If set to True,       listed file extensions will be excluded from the files to be uploaded
    #                   If set to False, ONLY listed file extensions will be included   in the files to be uploaded

    # Example call: getdir(sftp, "/local/path", "/remote/path", ".png", ".jpeg", exclude=False)

    for item in os.listdir(local_dir):
        local_item = os.path.join(local_dir, item)
        remote_item = posixpath.join(remote_dir, item)
        if os.path.isfile(local_item):
            if file_extensions is None:
                sftp.put(local_item, remote_item)
            else:  # Extensions specified
                file_extension = os.path.splitext(local_item)[-1]
                if exclude is False:
                    if file_extension in file_extensions:
                        sftp.put(local_item, remote_item)
                else:  # Exclude is True
                    if file_extension not in file_extensions:
                        sftp.put(local_item, remote_item)
        elif os.path.isdir(local_item):
            sftp.mkdir(remote_item)
            putdir(sftp, local_item, remote_item, file_extensions)
    return
