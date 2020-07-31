# Python Wake-on-LAN, CLI Function
# Python Module "wakeonlan" is required
# Visit https://pypi.org/project/wakeonlan/ to install module

import sys
from wakeonlan import send_magic_packet

print("Python wakeonlan module required")

#Input Ethernet MAC address
str_mac = input("Enter MAC Address ( Default address setting in source code ) : ")

if len(str_mac) == 0:
    #Default Mac address, if you are such a lazy guy
    def_str_mac = "1A-1B-4C-5D-1E-4F"
    separate = def_str_mac[2]
    str_mac = def_str_mac.replace(separate, "")
    
elif len(str_mac) == 17:
    #Convert string
    separate = str_mac[2]
    str_mac = str_mac.replace(separate, "")

elif len(str_mac) != 12:
    #Print error massage if format incorrect
    print("MAC Address format incorrect")

#Default is broadcast mode
str_ip = input(("Enter IP Address ( Default is Broadcast ) : ") or "255.255.255.255")

#Sending Magic Packet
send_magic_packet(str_mac, ip_address=str_ip, port=9)

#Print success massage
print("Magic Packet Sending Success")

sys.exit(0)
