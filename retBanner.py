#!/usr/bin/python

import socket

def retBanner(ip,port):
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((ip,port))
		banner = s.recv(1024)
		return banner
        except:
                return

def main():
        ip = raw_input("[*] Enter Target IP: ")
        for port in range(1,65536):
	        banner = retBanner(ip,port)
	        if banner:
        	        print "[+]" + ip + "/" + str(port) +  ": " + banner.strip('/n')

main()




