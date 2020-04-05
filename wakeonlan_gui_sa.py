import tkinter as tk
import socket
import binascii
import struct
import re
import tkinter as tk

#Main_Windows_Setting
window = tk.Tk()
window.title('Wake-on-LAN')
window.minsize(300,188)
window.maxsize(300,188)
window.grid_columnconfigure(0, weight=1)


#Exit_Button_Command_Definite
def close_window (): 
    window.destroy()

#Main_windows_Loop
window.mainloop()
