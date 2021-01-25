#coding=utf-8
import sys
import time
import socket
import datetime

#Time function
def time_log():
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d %H:%M:%S')

#Default MAC address
default = "5e:bd:ef:3c:38:35"
#Default sending port
str_port = 9

#Show notify
time_initia = time_log()
print(f"{time_initia} | Python wakeonlan")

#Input Ethernet MAC address
str_mac = input("Enter MAC Address: ")
#Input IP Address
str_ip = input("Enter IP Address ( Default is Broadcast ) : ")

#Default is broadcast mode
if len(str_ip) == 0:
    str_ip = "255.255.255.255"
else:
    pass

#Use default MAC address
if len(str_mac) == 0:
    separate = default[2]
    str_mac = default.replace(separate, "")
    time_usedef = time_log()
    print(f"{time_usedef} | Use Default MAC Address")
#Trans input mac adress
elif len(str_mac) == 17:
    separate = str_mac[2]
    str_mac = str_mac.replace(separate, "")
#Pass if omit separate
elif len(str_mac) == 12:
    pass
#Print error massage if format incorrect
else:
    time_macchk = time_log()
    print(f"{time_macchk} | MAC Address format incorrect")
    sys.exit(0)

#Convert input mac adress string into bytes
try:
    bytes_mac = bytes.fromhex("F" * 12 + str_mac *16)
#If Mac address format incorrect
except ValueError:
    time_macchk = time_log()
    print(f"{time_macchk} | MAC Address format incorrect")
    sys.exit(0)

try:
    #Send packet to ip address
    time_success = time_log()
    print(f"{time_success} | Magic Packet Sending ...")
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    soc.sendto(bytes_mac,(str_ip,str_port))
    #Wait
    time.sleep(1)
    soc.sendto(bytes_mac,(str_ip,str_port))
    #Close sending procress
    soc.close()
    #Print success massage
    time_closed = time_log()
    print(f"{time_closed} | Magic Packet Sending Success")
    sys.exit(0)

except Exception as error:
    time_error = time_log()
    print(f"{time_error} | Error occurred \r\n{error}")
    sys.exit(0)
