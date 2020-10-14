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

#Check input mac adress
def check_mac():
    #Get MAC address
    str_mac = text_mac.get()
    
    #Default MAC address
    default = "5e:bd:ef:3c:38:35"

    #Use default MAC address
    if len(str_mac) == 0:
        separate = default[2]
        str_mac = default.replace(separate, "")
        input_status.set("   Use Default MAC Address   ")
    #Trans input mac adress
    elif len(str_mac) == 17:
        separate = str_mac[2]
        str_mac = str_mac.replace(separate, "")
        input_status.set("  MAC Address Check Complete  ")
    #Pass if omit separate
    elif len(str_mac) == 12:
        pass
    
    #Convert input mac adress string into bytes
    try:
        return bytes.fromhex("F" * 12 + str_mac *16)
    #If Mac address format incorrect
    except ValueError:
        input_status.set(" MAC Address Format Incorrect ")
    
#Definite WakeUp command
def wake_up():
    #Default sending port
    str_port = 9
    #Get IP address
    str_ip = text_ip.get()
    
    #Default is broadcast mode
    if len(str_ip) == 0:
        str_ip = "255.255.255.255"
    else:
        pass

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

    except Exception:
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
text_ip.grid(row=5, ipadx=5, pady=5)

#Definite wakeUp command
buttonWake = tk.Button(window, text="Wake", width=20, command=wake_up)
buttonWake.grid(row=6, ipadx=5, pady=5)

#Definite exit button
buttonEnd = tk.Button(window, text="Exit", width=20, command=close_window)
buttonEnd.grid(row=7, ipadx=5, pady=5)

#Loop
window.mainloop()
