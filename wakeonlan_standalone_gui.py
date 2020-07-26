#coding=utf-8
#Python Wake-on-LAN, GUI Function

import sys
import time
import socket
import tkinter as tk

#Main windows, tkinter setting
window = tk.Tk()
window.title('Wake-on-LAN')
window.minsize(300,300)
window.maxsize(300,300)
window.grid_columnconfigure(0, weight=1)

#Setting textvariable status
global input_status
input_status = tk.StringVar()
status = tk.Label(window, textvariable=input_status)
status.grid(row=3, ipadx=5, pady=5)

#Exit button command definite
def close_window (): 
    window.destroy()

#Default
def check_mac():
    #Get MAC address
    str_mac = text_mac.get()

    #Check input mac adress
    if len(str_mac) == 17:
        separate = str_mac[2]
        str_mac = str_mac.replace(separate, "")
        input_status.set("  MAC Address Check Complete  ")

    #If Mac address format incorrect
    elif len(str_mac) != 12:
        input_status.set(" MAC Address Format Incorrect ")
    
    #Convert input mac adress string into bytes
    return bytes.fromhex("F" * 12 + str_mac *16)

#Definite WakeUp command
def wake_up():
    #Default sending port
    str_port = 9
    #Get IP address
    str_ip = text_ip.get()
    #Get bytes from check_mac
    bytes_mac = check_mac()

    try:
        #Setting socket
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
        #Start sending magic packet
        soc.sendto(bytes_mac,(str_ip,str_port))
        #Wait
        time.sleep(1)
        soc.sendto(bytes_mac,(str_ip,str_port))
        #Wait
        time.sleep(1)
        soc.sendto(bytes_mac,(str_ip,str_port))
        #Close sending procress
        soc.close()
        #Show success massage
        input_status.set(" Magic Packet Sending Success ")

    except ValueError:
        #If Mac address format or something incorrect
        input_status.set("Sending Fail, Something Wrong")

#Definite top description
label = tk.Label(window, text='Enter MAC Address')
label.grid(row=0, ipadx=5, pady=5)

#Definite Mac address input entry
text_mac = tk.Entry(window, justify='center')
text_mac.grid(row=1, ipadx=5, pady=5)

#Definite Check MAC Address command
buttonWake = tk.Button(window, text="Check MAC Address", width=20, command=check_mac)
buttonWake.grid(row=2, ipadx=5, pady=5)

#Definite top description
label = tk.Label(window, text='Enter IP Address ( Default is Broadcast )')
label.grid(row=4, ipadx=5, pady=5)

#Definite IP address input entry, Default is broadcast mode
text_ip = tk.Entry(window, justify='center')
text_ip.insert(0, "255.255.255.255")
text_ip.grid(row=5, ipadx=5, pady=5)

#Definite wakeUp command
buttonWake = tk.Button(window, text="Wake", width=20, command=wake_up)
buttonWake.grid(row=6, ipadx=5, pady=5)

#Definite exit button
buttonEnd = tk.Button(window, text="Exit", width=20, command=close_window)
buttonEnd.grid(row=7, ipadx=5, pady=5)

#Loop
window.mainloop()
