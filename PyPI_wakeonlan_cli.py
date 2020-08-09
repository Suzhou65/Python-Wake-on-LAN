# Python Wake-on-LAN, CLI Function
# Python Module "wakeonlan" is required
# Visit https://pypi.org/project/wakeonlan/ to install module
import sys
import datetime
from wakeonlan import send_magic_packet

#Time function
def time_log():
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d %H:%M:%S')

#Show notify
time_initia = time_log()
print(f"{time_initia} | Python wakeonlan module required")

#Input IP Address
str_ip = input("Enter  ( Default is Broadcast ) : ")

#Input Ethernet MAC address
str_mac = input("Enter MAC Address: ")

if len(str_mac) == 17:
    #Convert string
    separate = str_mac[2]
    str_mac = str_mac.replace(separate, "")

elif len(str_mac) != 12:
    #Print error massage if format incorrect
    time_macchk = time_log()
    print(f"{time_macchk} | MAC Address format incorrect")

#Default is broadcast mode
if len(str_ip) == 0:
    str_ip = "255.255.255.255"
else:
    pass

#Sending Magic Packet
send_magic_packet(str_mac, ip_address=str_ip, port=9)
time_closed = time_log()
print(f"{time_closed} | Magic Packet Sending Success")

sys.exit(0)
