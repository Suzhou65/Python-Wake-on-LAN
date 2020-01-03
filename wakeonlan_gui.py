# Python Wake-on-LAN, GUI Function
# Python Module "wakeonlan" is required
# Visit https://pypi.org/project/wakeonlan/ to install module

from wakeonlan import send_magic_packet
import tkinter as tk

#Main_Windows_Setting
window = tk.Tk()
window.title('Wake-on-LAN')
window.geometry('300x200')
window.resizable(False, False)

#Exit_Button_Command_Definite
def close_window (): 
    window.destroy()

#Definite_WakeUp_Command
def wake_up():
    #Get_Mac_address
    str_mac = e.get()
    #Broadcast_Range
    str_ip = "255.255.255.255"
    try:
        send_magic_packet(str_mac, ip_address=str_ip, port=9)
        status = tk.Label(window, text="Sending Success")
        status.grid(row=4, ipadx=5, pady=5)
        #IF_Sending_Success
    except:
        status = tk.Label(window, text="Sending Fail")
        status.grid(row=4, ipadx=5, pady=5)
        #If_Mac_Address_Format_Incorrect

#Definite_Input_Entry
#Definite_Mac
e = tk.Entry(window)
e.grid(column=0, row=0, ipadx=5, pady=5)

#Definite_WakeUp_Command
buttonWake = tk.Button(window, text="Wake", width=20, command=wake_up)
buttonWake.grid(row=1, ipadx=5, pady=5)

#Definite_Description
label = tk.Label(window, text='python wakeonlan module required\nMac address format 00:00:00:00:00:00')
label.grid(row=2, ipadx=5, pady=5)

#Definite_Exit_Button
buttonEnd = tk.Button(window, text="Exit", width=20, command=close_window)
buttonEnd.grid(row=3, ipadx=5, pady=5)

#Main_windows_Loop
window.grid_columnconfigure(0, weight=1)
window.mainloop()
