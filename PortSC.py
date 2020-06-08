#Programmer : Amin Asadi
#instagram : @aminasadiam
#twitter : @aminasadiam

# Import the librarys

import socket
import subprocess
import sys
from datetime import datetime

# use a subprocess

subprocess.call("clear" or "cls")

# Colors

class color:
	GREEN = '\033[92m'
	RED = '\033[91m'
	WHITE = '\033[0m'

# header

header = """
    ██████╗  ██████╗ ██████╗ ████████╗ ███████╗
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝ ██╔════╝
    ██████╔╝██║   ██║██████╔╝   ██║    ███████╗
    ██╔═══╝ ██║   ██║██╔══██╗   ██║    ╚════██║
    ██║     ╚██████╔╝██║  ██║   ██║    ███████║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚══════╝

"""

print(color.GREEN, header)

# input the information

target = input("Enter your Target for Start Scan >> ")
ip = socket.gethostbyname(target)

print("-" * 50)
print(color.RED, "Your Target ip --> ", ip)

print("-" * 50)
# start scaned time

t1 = datetime.now()


# start scan ports

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(color.WHITE, "port {} --------------------- open".format(port))
            sock.close()


except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()


# stop scaned time

t2 = datetime.now()

# result time scaned

t3 = t2 - t1

# Printing the information to screen

print(color.GREEN, 'Scanning Completed in: ', t3)

# Programming by : Amin Asadi
