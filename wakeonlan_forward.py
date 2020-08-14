#coding=utf-8
import os
import csv
import time
import socket
import datetime

#Time function
def time_log():
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d %H:%M:%S')

#Host check
def host_info():
    host_name = socket.gethostname()
    get_ip = socket.gethostbyname(host_name)
    #check get localhost ip address or not
    if get_ip == '127.0.1.1' or '127.0.0.1':
        check_host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        check_host.connect(("8.8.8.8", 80))
        return check_host.getsockname()[0]
    else:
        return socket.gethostbyname(host_name)

global magic_packet
#Translate MAC address
def packet2address():
    receive_packet = magic_packet.hex()
    packet_list = [receive_packet[i:i+12]
                   for i in range(0, len(receive_packet), 12)]
    address_string = packet_list[1]
    address_length, spliter = len(address_string), len(address_string)/6
    spliter = int(spliter)
    address_list = [address_string [i:i+spliter]
                    for i in range(0, address_length, spliter)]
    address_spliter = "-"     
    return address_spliter.join(address_list)

#Create record file
try:
    time_initia = time_log()
    #If exist, end check process
    record = open('wakeup_record.csv', mode='r')
    content = record.read()
    record.close()
    print(f"{time_initia} | Initialize complete")
except FileNotFoundError:
    #If not exist, create it
    with open('wakeup_record.csv', mode='w') as initialize_record:
        record = csv.writer(initialize_record, delimiter=',')
        record.writerow(['Receive time','MAC address','Description'])
        record.writerow([time_initia,'','initialize'])
        print(f"{time_initia} | Initialize complete. Record file create")

receive_host = host_info()
time_start = time_log()
#Root privileges check
try:
    #Receiving socket
    receive_protocol = 9
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    receive_socket.bind((receive_host, receive_protocol))
    #Print monitoring host if ready to go
    print (f"{time_start} | Now monitoring {receive_host}")
except PermissionError:
    #Ports below 1024 require root privileges, print alert message
    print(f"{time_start} | Ports below 1024 are privileged, require root privileges !")
    os._exit(0)

#Broadcast socket
broadcast_protocol = 7
broadcast = '255.255.255.255'
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
#Forwarding
try:
    #Recording start time
    with open('wakeup_record.csv', mode='a') as record_file:
        recording=csv.writer(record_file)
        time_record_start = time_log()
        recording.writerow([time_record_start,'','start'])
        record_file.flush()
        while True:
            #Receiving
            magic_packet, addr = receive_socket.recvfrom(2048)
            #If receiving Magic Packet
            if magic_packet is not None:
                #Recording wakeup event
                time_receive = time_log()
                mac_address = packet2address()
                recording.writerow([time_receive,mac_address,'receive'])
                record_file.flush()
                print(f"{time_receive} | Receiving {mac_address} ")
                #Sending receive magic packet once
                broadcast_socket.sendto(magic_packet,(broadcast, broadcast_protocol))
            else:
                continue
except KeyboardInterrupt:
    #Crtl+C to exit
    with open('wakeup_record.csv', mode='a') as record_file:
        closing=csv.writer(record_file)
        receive_socket.close()
        time_ending = time_log()
        closing.writerow([time_ending,'','quit'])
        print(f"\r\n{time_ending} | Thanks for using Wakeup forwarding ...")
