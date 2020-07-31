#coding=utf-8

import sys
import time
import socket

#Default sending port
str_port = 9

#Input IP Address
#Default is broadcast mode
str_ip = input(("Enter IP Address ( Default is Broadcast ) : ") or "255.255.255.255")

#Input Ethernet MAC address
str_mac = input("Enter MAC Address ( Default address setting in source code ) : ")

if len(str_mac) == 0:
    #Default Mac address, if you are such a lazy guy
    def_str_mac = "1A-1B-4C-5D-1E-4F"
    separate = def_str_mac[2]
    str_mac = def_str_mac.replace(separate, "")

elif len(str_mac) == 17:
    #Trans input mac adress
    separate = str_mac[2]
    str_mac = str_mac.replace(separate, "")

elif len(str_mac) != 12:
    #Print error massage if format incorrect
    print("MAC Address format incorrect")

#Convert input mac adress string into bytes
bytes_mac = bytes.fromhex("F" * 12 + str_mac *16)

#Send packet to ip address
print("Magic Packet Sending ...")
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
soc.sendto(bytes_mac,(str_ip,str_port))
#Wait
time.sleep(1)
soc.sendto(bytes_mac,(str_ip,str_port))
#Wait
time.sleep(1)
soc.sendto(bytes_mac,(str_ip,str_port))
#Close sending procress
soc.close()
#Print success massage
print("Magic Packet Sending Success")

sys.exit(0)