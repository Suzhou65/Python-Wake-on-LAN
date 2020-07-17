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

#Exit button command definite
def close_window (): 
    window.destroy()

#definite WakeUp command
def wake_up():
    #Get Mac address
    str_mac = text_mac.get()
    str_mac = str_mac.replace(':','-')
    #Broadcast range
    str_ip = text_ip.get()
    try:
        send_magic_packet(str_mac, ip_address=str_ip, port=9)
        status = tk.Label(window, text="Magic Packet Sending Success")
        status.grid(row=4, ipadx=5, pady=5)
        #If sending success
    except:
        status = tk.Label(window, text="Magic Packet Sending Fail")
        status.grid(row=4, ipadx=5, pady=5)
        #If Mac address format or something incorrect

#Definite top description
label = tk.Label(window, text='Python wakeonlan module required')
label.grid(row=0, ipadx=5, pady=5)

#Definite input entry
#Definite Mac address
text_mac = tk.Entry(window, justify='center')
text_mac.insert(0, "Mac address")
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
