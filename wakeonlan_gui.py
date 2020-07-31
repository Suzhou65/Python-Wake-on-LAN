# Python Wake-on-LAN, GUI Function
# Python Module "wakeonlan" is required
# Visit https://pypi.org/project/wakeonlan/ to install module

from wakeonlan import send_magic_packet
import tkinter as tk

#Main windows, tkinter setting
window = tk.Tk()
window.title('Wake-on-LAN')
window.minsize(300,240)
window.maxsize(300,240)
window.grid_columnconfigure(0, weight=1)

#Setting textvariable status
global status_lab
status_lab = tk.StringVar()
status = tk.Label(window, textvariable=status_lab)
status.grid(row=4, ipadx=5, pady=5)

#Exit button command definite
def close_window (): 
    window.destroy()

#definite WakeUp command
def wake_up():

    #Get Mac address
    str_mac = text_mac.get()
    
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
        status_lab.set("MAC Address format incorrect, sending Fail")

    #Broadcast range
    str_ip = text_ip.get()
    try:
        send_magic_packet(str_mac, ip_address=str_ip, port=9)
        status_lab.set("        Magic Packet Sending Success        ")
        #If sending success
    except ValueError:
        #If Mac address format or something incorrect
        status_lab.set("        Sending Fail, Something Wrong        ")

#Definite top description
label = tk.Label(window, text='Enter MAC address')
label.grid(row=0, ipadx=5, pady=5)

#Definite input entry
#Definite Mac address
text_mac = tk.Entry(window, justify='center')
text_mac.grid(row=1, ipadx=5, pady=5)

#Definite input entry
#Definite IP address
text_ip = tk.Entry(window, justify='center')
#Default is broadcast mode
text_ip.insert(0, "255.255.255.255")
text_ip.grid(row=2, ipadx=5, pady=5)

#Definite wakeUp command
buttonWake = tk.Button(window, text="Wake", width=20, command=wake_up)
buttonWake.grid(row=3, ipadx=5, pady=5)

#Definite exit button
buttonEnd = tk.Button(window, text="Exit", width=20, command=close_window)
buttonEnd.grid(row=5, ipadx=5, pady=5)

#Loop
window.mainloop()
