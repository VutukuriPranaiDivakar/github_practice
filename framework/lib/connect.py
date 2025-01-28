import paramiko
import json

with open(r"C:\Users\prana\OneDrive\Desktop\Webdevelopment\framework\testcases\config_files\host_details.json") as json_file:
        json_file = json.load(json_file)

ip_address = json_file["ip_address"]
username = json_file["username"]
port = 22
password = json_file["password"]

class connect:

    def __init__(self, ipaddress, username,password,port):
        self.ipaddress = ipaddress
        self.username = username
        self.password = password
        self.port = port
    
    def exec_cmd(self,cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(self.ipaddress, port=22, username=self.username, password=self.password, timeout=3)

        stdin , stdout, stderr = ssh.exec_command(self.cmd)

        if not stderr:
            return stdout.read()
        else:
            stderr.read()

    

    # def exec_cmd(cmd):

    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #     ssh.connect(ipaddress, port=22, username=username, password=password, timeout=3)

    #     stdin , stdout, stderr = ssh.exec_command(self.cmd)

    #     if not stderr:
    #         return stdout.read()
    #     else:
    #         stderr.read()



# import paramiko
# import json

# # Load host details from the JSON file
# with open(r"C:\Users\prana\OneDrive\Desktop\Webdevelopment\framework\testcases\config_files\host_details.json") as json_file:
#     host_details = json.load(json_file)

# # Extract connection details from the JSON data
# ip_address = host_details["ipaddress"]  # Correct key for IP address
# hostname = host_details["hostname"]
# username = host_details["username"]
# password = host_details["password"]
# port = host_details["port"]  # Port is also defined in the JSON file

# # Function to execute a command on the remote host
# def exec_cmd(cmd):
#     # Create SSH client instance
#     ssh = paramiko.SSHClient()
#     # Automatically add the host key (not recommended for production)
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#     try:
#         # Connect to the remote host using values from the JSON file
#         ssh.connect(hostname=ip_address, port=port, username=username, password=password, timeout=3)

#         # Execute the command
#         stdin, stdout, stderr = ssh.exec_command(cmd)

#         # Get the output from stdout and stderr
#         output = stdout.read().decode()
#         error = stderr.read().decode()

#         # Close the SSH connection
#         ssh.close()

#         # Return the output or error
#         if error:
#             return f"Error: {error}"
#         return output

#     except Exception as e:
#         return f"Connection failed: {str(e)}"

# # Example usage
# command = "show ip interface brief"
# result = exec_cmd(command)
# print(result)
