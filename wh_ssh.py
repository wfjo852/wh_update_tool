import paramiko
from scp import SCPClient, SCPException

class SSHManager:
    # """
    # usage:
    #     >>> import SSHManager
    #     >>> ssh_manager = SSHManager()
    #     >>> ssh_manager.create_ssh_client(hostname, username, password)
    #     >>> ssh_manager.send_command("ls -al")
    #     >>> ssh_manager.send_file("/path/to/local_path", "/path/to/remote_path")
    #     >>> ssh_manager.get_file("/path/to/remote_path", "/path/to/local_path")
    #     ...
    #     >>> ssh_manager.close_ssh_client()
    # """
    def __init__(self):
        self.ssh_client = None

    def create_ssh_client(self, hostname, port, username, password):
        """Create SSH client session to remote server"""

        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=hostname, port=port, username=username, password=password)

        # if self.ssh_client is None:
        #     self.ssh_client = paramiko.SSHClient()
        #     self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #     self.ssh_client.connect(hostname=hostname, port=port, username=username, password=password)
        # else:
        #     print("SSH client session exist.")

    def close_ssh_client(self):
        """Close SSH client session"""
        self.ssh_client.close()

    def send_file(self, local_path, remote_path):
        """Send a single file to remote path"""
        try:
            with SCPClient(self.ssh_client.get_transport()) as scp:
                scp.put(local_path, remote_path, recursive= False , preserve_times=True)
        except SCPException:
            raise SCPException.message

    def send_directory(self, local_path, remote_path):
        """Send a single file to remote path"""
        try:
            with SCPClient(self.ssh_client.get_transport()) as scp:
                scp.put(local_path, remote_path, recursive=True, preserve_times=True)
        except SCPException:
            raise SCPException.message


    def get_file(self, remote_path, local_path):
        """Get a single file from remote path"""
        try:
            with SCPClient(self.ssh_client.get_transport()) as scp:
                scp.get(remote_path, local_path)
        except SCPException:
            raise SCPException.message

    def send_command(self, command):
        """Send a single command"""
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.readlines()

