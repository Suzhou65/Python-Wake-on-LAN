# coding=utf-8
import sys
import wakeonlan
import tkinter as tk
# Main windows, tkinter setting
window = tk.Tk()
window.title('Wake-on-LAN')
window.minsize(300,300)
window.maxsize(300,300)
window.grid_columnconfigure(0, weight=1)
# Setting textvariable status
global input_status
input_status = tk.StringVar()
input_status.set("Ready")
status = tk.Label(window, textvariable=input_status)
status.grid(row=3, ipadx=5, pady=5)

# Exit button command definite
def close_window (): 
    window.destroy()

# Check input mac adress
def check_mac():
    global payload
    # Get MAC address
    address = text_mac.get()
    # Default MAC address
    if len(address) == 0:
        address = "FF:FF:FF:FF:FF:FF"
        payload = wakeonlan.address2packet(address)
        input_status.set("   Please input MAC Address   ")
        if type(payload) is bool:
            input_status.set("   Please input MAC Address   ")
        elif type(payload) is str:
            pass
    elif len(address) != 0:
        payload = wakeonlan.address2packet(address)
        if type(payload) is bool:
            # Print error massage if format incorrect
            input_status.set(" MAC Address Format Incorrect ")
        elif type(payload) is str:
            pass
# Definite WakeUp Event
def wake_up():
    # Get IP address
    broadcast_range = text_ip.get()
    # Default is broadcast mode
    if len(broadcast_range) == 0:
        # Broadcasting magic packet
        wakeonlan.packet_broadcasting(payload, default_config=True)
    elif len(broadcast_range) != 0:
        # Default sending port
        broadcast_protocol = 9
        # Sending magic packet
        wakeonlan.packet_broadcasting(payload, broadcast_range, broadcast_protocol)

#Definite top description
label = tk.Label(window, text='Enter MAC Address')
label.grid(row=0, ipadx=5, pady=5)
#Definite Mac address input entry
text_mac = tk.Entry(window, justify='center')
text_mac.grid(row=1, ipadx=5, pady=5)
#Definite Check MAC Address command
buttonWake = tk.Button(window, text="Load MAC Address", width=20, command=check_mac)
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
