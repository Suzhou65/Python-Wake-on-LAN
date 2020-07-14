# Python Wake-on-LAN, GUI Function
# Python Module "wakeonlan" is required
# Visit https://pypi.org/project/wakeonlan/ to install module

from wakeonlan import send_magic_packet
import tkinter as tk

#Main_Windows_Setting
window = tk.Tk()
window.title('Wake-on-LAN')
window.minsize(300,240)
window.maxsize(300,240)
window.grid_columnconfigure(0, weight=1)

#Exit_Button_Command_Definite
def close_window (): 
    window.destroy()

#Definite_WakeUp_Command
def wake_up():
    #Get_Mac_address
    str_mac = f1.get()
    str_mac = str_mac.replace(':','-')
    #Broadcast_Range
    str_ip = f2.get()
    try:
        send_magic_packet(str_mac, ip_address=str_ip, port=9)
        status = tk.Label(window, text="Magic Packet Sending Success")
        status.grid(row=4, ipadx=5, pady=5)
        #IF_Sending_Success
    except:
        status = tk.Label(window, text="Magic Packet Sending Fail")
        status.grid(row=4, ipadx=5, pady=5)
        #If_Mac_Address_Format_Incorrect

#Definite_Description
label = tk.Label(window, text='python wakeonlan module required')
label.grid(row=0, ipadx=5, pady=5)

#Definite_Input_Entry
#Definite_Mac
f1 = tk.Entry(window, justify='center')
f1.grid(row=1, ipadx=5, pady=5)

f2 = tk.Entry(window, justify='center')
f2.insert(0, "255.255.255.255")
f2.grid(row=2, ipadx=5, pady=5)

#Definite_WakeUp_Command
buttonWake = tk.Button(window, text="Wake", width=20, command=wake_up)
buttonWake.grid(row=3, ipadx=5, pady=5)

#Definite_Exit_Button
buttonEnd = tk.Button(window, text="Exit", width=20, command=close_window)
buttonEnd.grid(row=5, ipadx=5, pady=5)

#Main_windows_Loop
window.mainloop()
