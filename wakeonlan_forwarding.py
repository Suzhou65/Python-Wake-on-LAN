# -*- coding: utf-8 -*-
import sys
import socket
import wakeonlan

# Whitelist path
FilterPath = "/file_path/wakeonlan.whitelist.json"
# MAC address input recoed
RecordPath = "/file_path/wakeonlan.mac_address.csv"
# Program status file and path
StatusPath = "/file_path/wakeonlan.forward_status.csv"
# Forwarding target, Default is 255.255.255.255
Address = None
# Forwarding output port number, Default is port 9
Port = None

# Runtime
try:
    # Initialize configuration file and log
    wakeonlan.RecordFileInitialize(RecordFile=RecordPath,StatusFile=StatusPath)
    # Initialize whitelist JSON file
    wakeonlan.WhitelistInitialize(Whitelist=FilterPath)
    # Get host info
    HostAddress = wakeonlan.NetEnvkCheck()
    # Socket configuration
    ListeningSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    HostProtocol = 7
    ListeningSocket.bind((HostAddress,HostProtocol))
    # Ready
    print(f"Now monitoring address: {HostAddress}\r\nPort number: {HostProtocol}\r\n\r\nPressing Ctrl+C to exit.\r\n")
    # Logging program status
    wakeonlan.StatusBooking(StatusFile=StatusPath,StatusLogging=("Script is running."))
    # Loop
    while True:
        # Listening
        ReceivingData, ReceivingAddress = ListeningSocket.recvfrom(128)
        # Receiving packet
        if ReceivingData is not None:
            TranslateResult = wakeonlan.BytesTranslatedintoAddress(ReceivingData)
            # Debug_print([TranslateResult,ReceivingAddress])
            wakeonlan.SocketForwarding(ForwardingPayload=TranslateResult,ForwardingCheck=FilterPath,ForwardingRecord=RecordPath,ForwardingAddress=Address,ForwardingPort=Port)
        # If not, keep listening
        else:
            continue
# Exit
except KeyboardInterrupt:
    ExitMessage = ("Script has been manually stopped.")
    wakeonlan.StatusBooking(StatusFile=StatusPath,StatusLogging=ExitMessage)
    print(f"\r\n{ExitMessage}\r\n")
    sys.exit(0)
# Ports below 1024 require root privileges
except PermissionError:
    PermissionMessage = ("Ports below 1024 are privileged, require root privilege.")
    wakeonlan.StatusBooking(StatusFile=StatusPath,StatusLogging=PermissionMessage)
    print(f"{PermissionMessage}\r\n")
    sys.exit(0)
# Something wrong
except Exception as ErrorHandling:
    ErrorMessage = ("Script has stopped working due to error.")
    wakeonlan.StatusBooking(StatusFile=StatusPath,StatusLogging=ErrorMessage)
    print(f"{ErrorMessage} Error handling output:\r\n{ErrorHandling}\r\n")
    sys.exit(0)

# 2024.04.06