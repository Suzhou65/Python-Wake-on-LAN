#coding=utf-8
import sys
import time
import socket
import datetime

#Time function
def time_log():
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d %H:%M:%S')

#Default sending port
str_port = 9

#Show notify
time_initia = time_log()
print(f"{time_initia} | Python wakeonlan")

#Input IP Address
str_ip = input("Enter IP Address ( Default is Broadcast ) : ")

#Input Ethernet MAC address
str_mac = input("Enter MAC Address: ")

#Default is broadcast mode
if len(str_ip) == 0:
    str_ip = "255.255.255.255"
else:
    pass

if len(str_mac) == 17:
    #Trans input mac adress
    separate = str_mac[2]
    str_mac = str_mac.replace(separate, "")

elif len(str_mac) != 12:
    #Print error massage if format incorrect
    time_macchk = time_log()
    print(f"{time_macchk} | MAC Address format incorrect")

#Convert input mac adress string into bytes
bytes_mac = bytes.fromhex("F" * 12 + str_mac *16)

#Send packet to ip address
time_success = time_log()
print(f"{time_success} | Magic Packet Sending ...")
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
soc.sendto(bytes_mac,(str_ip,str_port))
#Wait
time.sleep(2)
soc.sendto(bytes_mac,(str_ip,str_port))
#Close sending procress
soc.close()
#Print success massage
time_closed = time_log()
print(f"{time_closed} | Magic Packet Sending Success")

sys.exit(0)
