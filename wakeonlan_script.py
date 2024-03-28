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
    GUIMacAddress = TextMAC.get()
    # Get IP address
    GUIBroadcastAddress = TextIP.get()
    # Get port
    GUIPort = TextPort.get()
    # Using default MAC adress
    if len(GUIMacAddress) == 0:
        GUIMacAddress = DefaultAddress
    else:
        pass
    # Using default IP adress
    if len(GUIBroadcastAddress) == 0:
        GUIBroadcastAddress = None
    else:
        pass
    # Using default port
    if len(GUIPort) == 0:
        GUIPort = None
    else:
        pass
    # Translate and check
    PayloadString = wakeonlan.AddressTranslatedintoBytes(GUIMacAddress)
    # If format incorrect
    if type(PayloadString) is int:
        del GUIMacAddress
    # If format correct
    elif type(PayloadString) is bytes:
        wakeonlan.LocalBroadcasting(WakeupMacAddress=GUIMacAddress, AddressConfig=GUIBroadcastAddress, PortConfig=GUIPort)
        del GUIMacAddress, GUIBroadcastAddress, GUIPort

# WoL, CLI mode
def CLIAction(DefaultAddress):
    # Print start message
    StartTime = wakeonlan.GetTime()
    print(f"{StartTime} | Python wakeonlan\r\n")
    # MAC address
    TypingMacAddress = input(f"Enter MAC address, default is {DefaultAddress}: ")
    if TypingMacAddress == 0:
        CLIMacAddress = DefaultAddress
    else:
        CLIMacAddress = TypingMacAddress
    # Check MAC addrrss
    AddressTranslate = wakeonlan.AddressTranslatedintoBytes(CLIMacAddress)
    # Incorrect MAC address input
    if type(AddressTranslate) is int:
        return 401
    # Check pass
    elif type(AddressTranslate) is bytes:
        pass
    # Input IP address
    BroadcastAddress = input("Enter IP address, default is Broadcast: ")
    if len() == 0:
        BroadcastAddress = None
    else:
        pass
    # Input port config
    BroadcastPort = input("Enter Port number, default is port 9: ")
    if len(BroadcastPort) == 0:
        BroadcastPort = None
    else:
        pass
    # Broadcasting magic packet
    StartWakeUp = wakeonlan.GetTime()
    print(f"{StartWakeUp} | Magic Packet Broadcasting...")
    wakeonlan.LocalBroadcasting(CLIMacAddress, AddressConfig=BroadcastAddress, PortConfig=BroadcastPort)

# Runtime
try:
    # CLI mode
    if EnableGUI is False:
        CheckResult = CLIAction(DefaultAddress)
        if type(CheckResult) is int:
            print("MAC Address format incorrect, please retry.\r\n")
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
        ButtonWake.grid(row=7,ipadx=5,pady=5)
        # Exit button
        ButtonExit = tkinter.Button(WindowUI,text="Exit",width=20,command=GUIEnding)
        ButtonExit.grid(row=8,ipadx=5,pady=5)
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