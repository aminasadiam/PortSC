#Programmer : Amin Asadi
#instagram : @aminasadiam
#twitter : @aminasadiam

# Import the librarys

import socket
import subprocess
import sys
from datetime import datetime

# use a subprocess

subprocess.call("clear")

# input the information

target = input("Enter your Target for Start Scan >> ")
ip = socket.gethostbyname(target)

print("-" * 50)
print("Your Target ip --> ", ip)
print("-" * 50)
# start scaned time

t1 = datetime.now()


# start scan ports

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("port {} --------------------- open".format(port))
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

print('Scanning Completed in: ', t3)

# Programming by : Amin Asadi
