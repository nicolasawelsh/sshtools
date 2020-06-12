def system(ssh, command):
    # Executes a remote command and waits for completion

    (stdin, stdout, stderr) = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status != 0:
        print("Error: ", exit_status)
    return
