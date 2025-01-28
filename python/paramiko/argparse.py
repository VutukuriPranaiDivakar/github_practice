import argparse

parser = argparse.ArgumentParser()

out = parser.add_argument("ipaddress", help="ip address of remote system", default="yes")
parser.add_argument("password", help="Password of remote system", default="yes")
parser.add_argument("username", help="username of remote system", default="yes")
args = parser.parse_args()
print(args)