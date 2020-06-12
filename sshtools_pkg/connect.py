from getpass import getpass
import paramiko


def connect(host_ip, host_port, username=False, password=False):
    # Connect to server via SSH

    ssh = False
    connected = False
    print("Connecting to " + host_ip + ":" + str(host_port))
    while not connected:
        if not username:
            username = input("Enter your username: ")
        if not password:
            password = getpass("Enter your password: ")

        try:
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host_ip, host_port, username, password)
            connected = True
            print("Connection successful")
        except Exception as e:
            print(str(e))
    return ssh
