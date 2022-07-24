# -*- coding: utf-8 -*-
import sys
import csv
import socket
import wakeonlan

# Ignore wakeup all
ignroe_reveille = True
# program status file and path
path_status = "status_program.csv"
# wakeup record file and path
path_wakeup_record = "wakeup_record.csv"

# Initialize recording file
wakeonlan.program_status(path_status)
wakeonlan.record_tape(path_wakeup_record)
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
        wakeonlan.program_status(path_status, event="PermissionError")
        sys.exit(0)
    # Recording start time
    with open(path_wakeup_record, mode="a", newline="") as tape:
        recording=csv.writer(tape)
        print(f"{time_start} | Now monitoring {receive_host}, pressing CTRL+C to exit")
        wakeonlan.program_status(path_status, event="Now monitoring")
        # Ready
        while True:
            # Listening
            receiving, addr = receive_socket.recvfrom(128)
            if receiving is not None:
                time_receive = wakeonlan.stamp()
                # Translate bytes data to MAC
                address = wakeonlan.packet2address(receiving)
                # Check
                if type(address) is bool:
                    # Omit incorrect
                    recording.writerow([time_receive,"Omit"])
                    tape.flush()
                    print(f"{time_receive} | Receiving incorrect data")
                elif type(address) is str:
                    broadcast_wakeup = "ff-ff-ff-ff-ff-ff"
                    if address == broadcast_wakeup and ignroe_reveille is True:
                        recording.writerow([time_receive,"Omit Reveille"])
                        tape.flush()
                        print(f"{time_receive} | Ignore wakeup all")
                    else:
                        # Translate MAC
                        payload = wakeonlan.address2packet(address)
                        # Socket config
                        broadcast_range = "255.255.255.255"
                        broadcast_protocol = 7
                        # Sending
                        wakeonlan.packet_broadcasting(payload, broadcast_range, broadcast_protocol)
                        # Print receiving
                        print(f"{time_receive} | Receiving {address}")
                        # Recording wakeup event
                        recording.writerow([time_receive,address])
                        tape.flush()        
            # If not, keep receiving
            else:
                continue
# Exit
except KeyboardInterrupt:
    manual_quit = wakeonlan.stamp()
    print(f"\r\n{manual_quit} | Thank you for using the Wakeup forwarding.\r\nGoodBye ...")
    wakeonlan.program_status(path_status, event="Program not running")
    sys.exit(0)
# If something wrong
except Exception as error_status:
    error_quit = wakeonlan.stamp()
    print(f"\r\n{error_quit} | Program stop running due to unexpected error.")
    wakeonlan.program_status(path_status, event="Error occurred")
    sys.exit(0)
