# -*- coding: utf-8 -*-
import sys
import tkinter
import wakeonlan

# GUI mode switch
EnableGUI = False
# Default MAC address
DefaultAddress = "FF:FF:FF:FF:FF:FF"

# Exit button definite
def GUIEnding(): 
    WindowUI.destroy()
    sys.exit(0)

# WoL, GUI mode
def GUIAction():
    # Get MAC address
    InputMacAddress = TextMAC.get()
    # Get IP address
    BroadcastAddress = TextIP.get()
    # Get port
    BroadcastPort = TextPort.get()
    # Using default MAC adress
    if str(InputMacAddress) == "":
        InputMacAddress = DefaultAddress
    else:
        pass
    # Using default IP adress
    if str(BroadcastAddress) == "":
        BroadcastAddress = None
    else:
        pass
    # Using default port
    if str(BroadcastPort) == "":
        BroadcastPort = None
    else:
        pass
    # Translate and check
    PayloadString = wakeonlan.AddressTranslatedintoBytes(InputMacAddress)
    # If format incorrect
    if type(PayloadString) is int:
        del InputMacAddress
    # If format correct
    elif type(PayloadString) is bytes:
        wakeonlan.LocalBroadcasting(InputMacAddress,AddressConfig=BroadcastAddress,PortConfig=BroadcastPort)
        del InputMacAddress,BroadcastAddress,BroadcastPort

# WoL, CLI mode
def WakeupScript(DefaultAddress):
    # MAC address
    InputMacAddress = input(f"Enter MAC address, default is {DefaultAddress} : ")
    # Default MAC address
    if str(InputMacAddress) == "":
        InputMacAddress = DefaultAddress
    else:
        pass
    # Check MAC addrrss
    AddressCheck = wakeonlan.AddressTranslatedintoBytes(InputMacAddress)
    # Incorrect MAC address input
    if type(AddressCheck) is int:
        return 401
    # Check pass
    elif type(AddressCheck) is bytes:
        # Input IP address
        BroadcastAddress = input("Enter IP address, default is Broadcast: ")
        if str(BroadcastAddress) == "":
            BroadcastAddress = None
        else:
            pass
        # Input port config
        BroadcastPort = input("Enter Port number, default is port 9: ")
        if str(BroadcastPort) == "":
            BroadcastPort = None
        else:
            pass
    # Broadcasting magic packet
        print("Magic Packet Broadcasting...")
        return wakeonlan.LocalBroadcasting(InputMacAddress,AddressConfig=BroadcastAddress,PortConfig=BroadcastPort)

# Runtime
try:
    # CLI mode
    if EnableGUI is False:
        CheckResult = WakeupScript(DefaultAddress)
        if type(CheckResult) is int:
            print("Error occurred, please retry.\r\n")
            sys.exit(0)
        else:
            SuccessTime = wakeonlan.GetTime()
            print(f"{SuccessTime} | Magic packet broadcast successfully.\r\n")
            sys.exit(0)
    # GUI, Tkinter mode
    elif EnableGUI is True:
        # Tkinter main windows configuration
        WindowUI = tkinter.Tk()
        WindowUI.title("Wake-on-LAN GUI")
        WindowUI.minsize(330,320)
        WindowUI.maxsize(330,320)
        WindowUI.grid_columnconfigure(0,weight=1)
        # Top description
        Label = tkinter.Label(WindowUI,text=f"Enter MAC address, default is {DefaultAddress}")
        Label.grid(row=0,ipadx=5,pady=5)
        # Mac address input entry
        TextMAC = tkinter.Entry(WindowUI,justify="center")
        TextMAC.grid(row=1,ipadx=5,pady=5)
        # Top description
        Label = tkinter.Label(WindowUI,text="Enter IP address, default is Broadcast")
        Label.grid(row=2,ipadx=5,pady=5)
        # IP address input entry, Default is broadcast mode
        TextIP = tkinter.Entry(WindowUI,justify="center")
        TextIP.grid(row=3,ipadx=5,pady=5)
        # Broadcasting port input entry
        Label = tkinter.Label(WindowUI,text="Enter broadcasting port, default is 9")
        Label.grid(row=4,ipadx=5,pady=5)
        # Mac address input entry
        TextPort = tkinter.Entry(WindowUI,justify="center")
        TextPort.grid(row=5,ipadx=5,pady=5)
        # Command
        ButtonWake = tkinter.Button(WindowUI,text="Wake",width=20,command=GUIAction)
        ButtonWake.grid(row=8,ipadx=5,pady=5)
        # Exit button
        ButtonExit = tkinter.Button(WindowUI,text="Exit",width=20,command=GUIEnding)
        ButtonExit.grid(row=9,ipadx=5,pady=5)
        # Loop Render
        WindowUI.mainloop()
# Command quit
except KeyboardInterrupt:
    print("Script ending. Goodbye...\r\n")
    sys.exit(0)
# Error
except Exception:
    print("Script has stopped working due to Error occurred.\r\n")
    sys.exit(0)

# 2024.03.28