import os
import posixpath


def putdir(sftp, local_dir, remote_dir, *file_extensions):
    # Recursively upload dir from local to remote
    # argv: List of extensions to ignore in upload (will upload all if left blank)
    # Example: putdir(sftp, "C:/example_dir", "/mnt/example_dir", ".fig", ".png")

    for item in os.listdir(local_dir):
        local_item = posixpath.join(local_dir, item)
        remote_item = posixpath.join(remote_dir, item)
        if os.path.isfile(local_item):
            if file_extensions is None:
                sftp.put(local_item, remote_item)
            else:
                file_extension = os.path.splitext(local_item)[-1]
                if file_extension not in file_extensions:
                    sftp.put(local_item, remote_item)
        elif os.path.isdir(local_item):
            sftp.mkdir(remote_item)
            putdir(sftp, local_item, remote_item, file_extensions)
    return
