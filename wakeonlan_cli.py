# Python Wake-on-LAN, CLI Function
# Python Module "wakeonlan" is required
# Visit https://pypi.org/project/wakeonlan/ to install module

import sys
from wakeonlan import send_magic_packet

#Input Ethernet MAC address
str_mac = input("Enter Ethernet MAC Address: ")

#Translate string
str_mac = str_mac.replace(':','-')

#Default is broadcast mode
str_ip = input(("Enter IP Address ( Default is Broadcast ) : ") or "255.255.255.255")

#Sending Magic Packet
send_magic_packet(str_mac, ip_address=str_ip, port=9)

#Print success massage
print("Magic Packet Sending Success")

sys.exit(0)
