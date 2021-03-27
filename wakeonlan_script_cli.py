#coding=utf-8
import sys
import wakeonlan
# Show notify
time_initia = wakeonlan.stamp()
print(f"{time_initia} | Python wakeonlan")
# Input Ethernet MAC address
address = input("Enter MAC Address: ")
# Use default MAC address
if len(address) == 0:
    # Default MAC address
    address = "5E:BD:EF:3C:38:35"
    time_usedef = wakeonlan.stamp()
    payload = wakeonlan.address2packet(address)
    print(f"{time_usedef} | Use Default MAC Address")
elif len(address) != 0:
    payload = wakeonlan.address2packet(address)
# Print error massage if format incorrect
if type(payload) is bool:
    time_macchk = wakeonlan.stamp()
    print(f"{time_macchk} | MAC Address format incorrect")
    sys.exit(0)
elif type(payload) is str:
    pass
# Input IP Address
time_sending = wakeonlan.stamp()
broadcast_range = input("Enter IP Address ( Default is Broadcast ) : ")
# Default is broadcast config
if len(broadcast_range) == 0:
    # Broadcasting magic packet
    wakeonlan.packet_broadcasting(payload, default_config=True)
    print(f"{time_sending} | Magic Packet Broadcasting ...")
    sys.exit(0)
elif len(broadcast_range) != 0:
    # Send packet to ip address
    broadcast_protocol = 9
    wakeonlan.packet_broadcasting(payload, broadcast_range, broadcast_protocol)
    print(f"{time_sending} | Magic Packet Sending ...")
    sys.exit(0)
