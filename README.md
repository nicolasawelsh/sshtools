# sshtools

## A package of tools involved in server connection and management

**connect**(*host_ip, host_port, username=False, password=False*)
> **Description:**
> * Connect to server via SSH

> **Parameters**
> * **host_ip** (str) - server ip to connect to
> * **host_port** (int) - server port to connect to
> * **username** (str) - username to authenticate as
> * **password** (str) - password for authentification

**system**(*ssh, cmmand*)
> **Description:**
> * Executes a remote command and waits for completion

> **Parameters**
> * **ssh** - ssh client
> * **host_port** (str) - specified command

**getdir**(*sftp, remote_dir, local_dir, *file_extensions, exclude=True*)

**putdir**(*sftp, local_dir, remote_dir, *file_extensions, exclude=True*)

**rmdir**(*sftp, remote_path, level=0*)
