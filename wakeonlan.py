# -*- coding: utf-8 -*-
import csv
import socket
import datetime

# Defult program status file and path
defult_path_status = "status_program.csv"
# Defult wakeup record file and path
defult_path_wakeup_record = "wakeup_record.csv"

# Time function
def stamp():
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d %H:%M:%S')

# Program Status
def program_status( path_status=() ,event=() ):
    if bool(path_status) is False:
        path_status = defult_path_status
    elif bool(path_status) is True:
        pass
    # header
    ststus_header = ["Time","Program Status"]
    # Status
    if bool(event) is False:
        status_table =  [stamp(),"Initialize"]
    elif bool(event) is True:
        status_table =  [stamp(), event]
    # Zipped
    rows = [ststus_header,status_table]
    # Create status file
    with open(path_status, "w", newline="") as status_file:
        status_tape = csv.writer(status_file)
        for row in rows:
            status_tape.writerow(row)
        status_file.close()
    return status_table

# Create recording
def record_tape( path_wakeup_record=() ):
    if bool(path_wakeup_record) is False:
        path_wakeup_record = defult_path_wakeup_record
    elif bool(path_wakeup_record) is True:
        pass
    time_initialize = stamp()
    # If exist, end check process
    try:
        record = open(path_wakeup_record, mode="r")
        print(f"{time_initialize} | Initialize complete")
        record.close()
        return True
    # If not exist, create it
    except FileNotFoundError:
        with open(path_wakeup_record, mode="w", newline="") as tape_initialize:
            record = csv.writer(tape_initialize, delimiter=",")
            record.writerow(["Time","Address"])
            print(f"{time_initialize} | Initialize complete. Record file create")
            tape_initialize.close()
            return False

# Host check
def host_info():
    host_name = socket.gethostname()
    get_ip = socket.gethostbyname(host_name)
    # check get localhost ip address or not
    if get_ip == '127.0.1.1' or '127.0.0.1':
        check_host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        check_host.connect(("8.8.8.8", 80))
        return check_host.getsockname()[0]
    else:
        return socket.gethostbyname(host_name)

# Translate MAC address to packet
def address2packet(address):
    # Trans input mac adress
    if len(address) == 17:
        separate = address[2]
        address = address.replace(separate, "")
    # Pass if omit separate
    elif len(address) == 12:
        pass
    # If format incorrect
    else:
        return True
    # Convert input mac adress string into bytes
    try:
        bytes_mac = bytes.fromhex("F" * 12 + address *16)
        return bytes_mac
    # If Mac address format incorrect
    except ValueError:
        return False

# Translate bytes to MAC address
def packet2address(receiving):
    decode_receiving = receiving.hex()
    try:
        packet_list = [decode_receiving[i:i+12]
            for i in range(0, len(decode_receiving),12)]
        address_string = packet_list[1]
        address_length, spliter = len(address_string),len(address_string)/6
        spliter = int(spliter)
        address_list = [address_string [i:i+spliter]
            for i in range(0, address_length, spliter)]
        address_spliter = "-"
        return address_spliter.join(address_list)
    #If data doesn't look like MAC address
    except Exception:
        return False

def packet_broadcasting(payload, default_config=(), broadcast_range=(), broadcast_protocol=() ):
    # Broadcast socket
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    if bool(default_config) is True:
        broadcast_range = "255.255.255.255"
        broadcast_protocol = 9
        # broadcasting
        broadcast_socket.sendto(payload,(broadcast_range, broadcast_protocol))
        broadcast_socket.close()
    else:
        # Sending
        broadcast_socket.sendto(payload,(broadcast_range, broadcast_protocol))
        broadcast_socket.close()
