#!/bin/python3

import sys  #command line arguments
import socket
from datetime import datetime

#Define target

python3 scanner.py <ip>
if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) #translate hostanme to IPV4
else:
        print("Invalid amount of arguements.")
        print("Syntax: python3 scanner.py <ip>")
        sys.exit()

#Add a banner
print("-" *50)
print("Scanning target" + target)
print("Time started" +str(datetime.now()))
print("-" * 50)

try:
        for port in range(50,85):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1) 
                result = s.connect_ex((target.port)) #return error
                print("Checking port {}".format(port))
                if result == 0:
                        print("Port {} is open".format(port))
                s.close()
                
except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
        
except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
        
except socket.error:
        print("Couldn't connect to server.")
        sys.exit()
