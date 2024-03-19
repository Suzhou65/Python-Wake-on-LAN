# -*- coding: utf-8 -*-
import sys
import wakeonlan
import tkinter

# GUI mode switch
EnableGUI = False
# Default MAC address
DefaultAddress = "00:11:AF:D6:A5:E2"

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
    # Using text input
    else:
        pass
    # Translate and check
    PayloadString = wakeonlan.Address2Packet(GUIMacAddress)
    # Print error massage if format incorrect
    if type(PayloadString) is bool:
        del GUIMacAddress
        pass
    # If format correct
    else:
        wakeonlan.LocalBroadcasting(PacketPayload=PayloadString,SelectAddress=GUIBroadcastAddress,SelectProtocolNumber=GUIPort)
        del GUIMacAddress, GUIBroadcastAddress, GUIPort

# WoL, CLI mode
def CLIAction(DefaultAddress):
    # Print start message
    StartTime = wakeonlan.GetTime()
    print(f"{StartTime} | Python wakeonlan\r\n")
    # MAC address
    TypingMacAddress = input(f"Enter MAC address, default is {DefaultAddress}: ")
    if TypingMacAddress == 0:
        MacAddress = DefaultAddress
    else:
        MacAddress = TypingMacAddress
    # Check MAC addrrss
    AddressTranslate = wakeonlan.Address2Packet(MacAddress)
    if type(AddressTranslate) is bool:
        return 401
    else:
        pass
    # Input IP address
    BroadcastAddress = input("Enter IP address, default is Broadcast: ")
    # Input port config
    BroadcastPort = input("Enter Port number, default is port 9: ")
    # Broadcasting magic packet
    StartWakeUp = wakeonlan.GetTime()
    print(f"{StartWakeUp} | Magic Packet Broadcasting...")
    wakeonlan.LocalBroadcasting(PacketPayload=AddressTranslate, SelectAddress=BroadcastAddress, SelectProtocolNumber=BroadcastPort)
    return AddressTranslate

# Runtime
try:
    if EnableGUI is False:
        CheckResult = CLIAction(DefaultAddress)
        if type(CheckResult) is int:
            print("MAC Address format incorrect, please retry.\r\n")
            sys.exit(0)
        else:
            SuccessTime = wakeonlan.GetTime()
            print(f"{SuccessTime} | Magic packet broadcast successfully.\r\n")
            sys.exit(0)
    elif EnableGUI is True:
        # Tkinter main windows configuration
        WindowUI = tkinter.Tk()
        WindowUI.title("Wake-on-LAN GUI")
        WindowUI.minsize(330,320)
        WindowUI.maxsize(330,320)
        WindowUI.grid_columnconfigure(0,weight=1)
        # Render, definite top description
        Label = tkinter.Label(WindowUI,text=f"Enter MAC address, default is {DefaultAddress}")
        Label.grid(row=0,ipadx=5,pady=5)
        # Definite Mac address input entry
        TextMAC = tkinter.Entry(WindowUI,justify="center")
        TextMAC.grid(row=1,ipadx=5,pady=5)
        # Definite top description
        Label = tkinter.Label(WindowUI,text="Enter IP address, default is Broadcast")
        Label.grid(row=2,ipadx=5,pady=5)
        # Definite IP address input entry, Default is broadcast mode
        TextIP = tkinter.Entry(WindowUI,justify="center")
        TextIP.grid(row=3,ipadx=5,pady=5)
        # Definite broadcasting port
        Label = tkinter.Label(WindowUI,text="Enter broadcasting port, default is 9")
        Label.grid(row=4,ipadx=5,pady=5)
        # Definite Mac address input entry
        TextPort = tkinter.Entry(WindowUI,justify="center")
        TextPort.grid(row=5,ipadx=5,pady=5)
        # Definite WOL command
        ButtonWake = tkinter.Button(WindowUI,text="Wake",width=20,command=GUIAction)
        ButtonWake.grid(row=7,ipadx=5,pady=5)
        # Definite exit button
        ButtonExit = tkinter.Button(WindowUI,text="Exit",width=20,command=GUIEnding)
        ButtonExit.grid(row=8,ipadx=5,pady=5)
        # Loop
        WindowUI.mainloop()
# Command Exit
except KeyboardInterrupt:
    print("Goodbye...\r\n")
    sys.exit(0)
except Exception:
    ErrorTime = wakeonlan.GetTime()
    print(f"{ErrorTime} | Error occurred.\r\n")
    sys.exit(0)

# 2024.03.19