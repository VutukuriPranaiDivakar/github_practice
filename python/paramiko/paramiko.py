"""
Paramiko :: 
            Module to connect remote hosts
            SSH Protocol for connection to remote host
            SFTP for tranferrign files between the servers

"""

import paramiko
import sys
import argparse

ipaddress = ""
port_num = 22
username = "winteck"
password = "Winteck@2024"

ipaddress = sys.argv[1]
port_num = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]


def exec_cmd(cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ipaddress, username=username, password=password, port=port_num)
    stdin, stout, stderr = client.exec_command(cmd)

print(exec_cmd("hostname"))
print(exec_cmd("uptime"))