#!/bin/bash
## Author: V1N4Y - White$Devil

import socket
import sys
from datetime import datetime

if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
		
else:
	print("Invalid arguments")
	print("Syntax: python3 portscanner.py 192.168.xx.xx")
	
#Banner

print("_" *50)
print(f"Scanning Ip: {target}")
print(f"Time: {datetime.now()}")
print("_" *50)


try:
	print("This will take a while....")
	print("Take a cup of coffee.")
	for port in range(50, 90):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		
		if result == 0:
			print(f"Port {port} is open")
			
		s.close()
		
except KeyboardInterrupt:
	print("\nExinting program....")
	sys.exit()

except socket.gaierror:
	print("Hostname could not resolve")
	sys.exit()
	
except socket.error:
	print("Could not connet to server")
	sys.exit()
