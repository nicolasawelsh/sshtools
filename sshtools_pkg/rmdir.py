from stat import S_ISDIR
import posixpath


def rmdir(sftp, remote_path, level=0):
    # Recursively delete remote dir

    for file in sftp.listdir_attr(remote_path):
        filepath = posixpath.join(remote_path, file.filename)
        if S_ISDIR(file.st_mode):
            rmdir(sftp, filepath, level=(level + 1))
        else:
            filepath = posixpath.join(remote_path, file.filename)
            sftp.remove(filepath)
    sftp.rmdir(remote_path)
    return
