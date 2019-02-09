#!/usr/bin/env python3
# Coded By : A_Asaker

import socket

def scan():
  for port in range(2**16-1):
  	try:
  		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  		s.bind(("",port))
  		s.close()
  	except Exception as ex:
  		print(port,":",ex)
if __name__ == "__main__":
  scan()
