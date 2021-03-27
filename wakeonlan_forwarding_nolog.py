#coding=utf-8
import sys
import socket
import wakeonlan

# Forwarding
try:
    time_start = wakeonlan.stamp()
    # Check permission
    try:
        # Get Host
        receive_host = wakeonlan.host_info()
        # Listening socket config
        receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        receive_protocol = 9
        receive_socket.bind((receive_host, receive_protocol))
    # If ports below 1024 require root privileges
    except PermissionError:
        print(f"{time_start} | Ports below 1024 are privileged, require root privileges !")
        sys.exit(0)
    # Print start time
    print(f"{time_start} | Now monitoring {receive_host}, pressing CTRL+C to exit")
    # Ready
    while True:
        # Listening
        receiving, addr = receive_socket.recvfrom(128)
        if receiving is not None:
            # Translate bytes data to MAC
            address = wakeonlan.packet2address(receiving)
            # Check
            if type(address) is bool:
                # Omit incorrect
                time_incorrect = wakeonlan.stamp()
                print(f"{time_incorrect} | Receiving incorrect data")
            elif type(address) is str:
                time_receive = wakeonlan.stamp()
                # Translate MAC
                payload = wakeonlan.address2packet(address)
                # Socket config
                broadcast_range = "255.255.255.255"
                broadcast_protocol = 7
                # Sending
                wakeonlan.packet_broadcasting(payload, broadcast_range, broadcast_protocol)
                # Print receiving
                print(f"{time_receive} | Receiving {address}")
        # If not, keep receiving
        else:
            continue
# Exit
except KeyboardInterrupt:
    ending = wakeonlan.stamp()
    print(f"\r\n{ending} | Thank you for using the Wakeup forwarding.\r\nGoodBye ...")
    sys.exit(0)
