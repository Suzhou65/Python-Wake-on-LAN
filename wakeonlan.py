# -*- coding: utf-8 -*-
import csv
import json
import socket
import logging
import datetime

# For error handling, logfile config
FORMAT = "%(asctime)s |%(levelname)s |%(message)s"
# Error logfile name and level config
logging.basicConfig(level=logging.WARNING,filename="wakeonlan.error.log",filemode="a",format=FORMAT)

# Generate timestamp
def GetTime():
    CurrentTime = datetime.datetime.now()
    return CurrentTime.strftime("%Y-%m-%d %H:%M:%S")

# Check wakeup event and status record file
def RecordFileInitialize(RecordFile=None, StatusFile=None):
    # Enable wakeup record
    if RecordFile is not None:
        try:
            CheckRecordFile = open(RecordFile,mode="r")
            CheckRecordFile.close()
        except FileNotFoundError:
            # Create csv file
            with open(RecordFile,mode="w",newline="") as RecordTapeInitialize:
                RecordTape = csv.writer(RecordTapeInitialize, delimiter=",")
                RecordTape.writerow(["Time","Address"])
                RecordTapeInitialize.close()
    # Disable wakeup record
    elif StatusFile is None:
        pass
    # Enable status logging
    if StatusFile is not None:
        try:
            CheckStatusFile = open(StatusFile,mode="r")
            CheckStatusFile.close()
        except FileNotFoundError:
            # Create csv file
            with open(StatusFile,mode="w",newline="") as StatusTapeInitialize:
                StatusTape = csv.writer(StatusTapeInitialize,delimiter=",")
                CreateStatusTapeTime = GetTime()
                StatusTape.writerow([CreateStatusTapeTime,"Initialization Complete"])
                StatusTapeInitialize.close()
    # Disable status logging
    elif bool(StatusFile) is False:
        pass

# Check whitelist file
def WhitelistInitialize(Whitelist=None):
    # Enable whitelist, check JSON file
    if Whitelist is not None:
        try:
            with open(Whitelist,"r") as WhitelistCheck:
                WhitelistCheck.close()
        # File not found
        except FileNotFoundError:
            # Create dictionary
            WhitelistDict = {"AllowAddress":[
                    "",
                    ""],
                "Comment":[
                    "USE CAPITAL CASE",
                    "IF YOU ALLOW WAKEUP ALL, ADD FF:FF:FF:FF:FF:FF INTO AllowAddress LIST"]}
            # Create JSON file
            with open(Whitelist,"w") as WhitelistCreate:
                json.dump(WhitelistDict,WhitelistCreate,indent=2)
                WhitelistCreate.close()
    # Disable whitelist functon
    elif Whitelist is None:
        pass

# Typing MAC address accepted
def WakeupBooking(RecordFile=None, AddressLogging=()):
    # Enable wakeup record
    if RecordFile is not None:
        try:
            AddressBookingTime = GetTime()
            AddressBookingRow = [AddressBookingTime,AddressLogging]
            # Writing to MAC address record
            with open(RecordFile,mode="a",newline="") as AddressBook:
                AddressTape = csv.writer(AddressBook,delimiter=",")
                AddressTape.writerow(AddressBookingRow)
                AddressBook.flush()
                AddressBook.close()
        except Exception as BookingError:
            logging.exception(BookingError)
            pass
    # Disable booking
    elif RecordFile is None:
        pass

# Program executive logging
def StatusBooking(StatusFile=None, StatusLogging=()):
    # Enable status booking
    if StatusFile is not None:
        try:
            StatusBookingTime = GetTime()
            StatusBookingRow = [StatusBookingTime,StatusLogging]
            # Writing status record
            with open(StatusFile,mode="w",newline="") as StatusBook:
                StatusTape = csv.writer(StatusBook, delimiter=",")
                StatusTape.writerow(StatusBookingRow)
                StatusBook.flush()
                StatusBook.close()
        except Exception as BookingError:
            logging.exception(BookingError)
            pass
    # Disable status booking
    elif StatusFile is None:
        pass

# Check LAN environment
def NetEnvkCheck():
    AskHostName = socket.gethostname()
    AskIP = socket.gethostbyname(AskHostName)
    # check get localhost ip address or not
    if AskIP == "127.0.1.1" or "127.0.0.1":
        CheckHost = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        CheckHost.connect(("8.8.8.8",80))
        return CheckHost.getsockname()[0]
    else:
        return socket.gethostbyname(AskHostName)

# Convert MAC address to bytes
def AddressTranslatedintoBytes(MacAddress):
    try:
        # With separate character
        if len(MacAddress) == 17:
            SeparateCharacter = MacAddress[2]
            # Remove separate character
            MacAddress = MacAddress.replace(SeparateCharacter,"")
            # Turn string into bytes
            BytesMacAddress = bytes.fromhex("F" * 12 + MacAddress *16)
            return BytesMacAddress
        # Without separate character
        elif len(MacAddress) == 12:
            BytesMacAddress = bytes.fromhex("F" * 12 + MacAddress *16)
            return BytesMacAddress
        # If format incorrect
        else:
            return 101
    except Exception as ConvertError:
        logging.exception(ConvertError)
        return 102

# Convert bytes to MAC address
def BytesTranslatedintoAddress(PacketInput):
    try:
        # Convert Hexadecimal
        DecodePacket = PacketInput.hex()
        # Recursion
        Decode2List = [DecodePacket[i:i+12]
            for i in range(0, len(DecodePacket),12)]
        # Get payload
        MacAddressString = Decode2List[1]
        # 
        StringLength, StringSpliter = len(MacAddressString),len(MacAddressString)/6
        StringSpliter = int(StringSpliter)
        AddressOutput = [MacAddressString [i:i+StringSpliter]
            for i in range(0, StringLength, StringSpliter)]
        # Separate character
        SpliterCharacter = ":"
        return SpliterCharacter.join(AddressOutput).upper()
    #If data doesn't look like MAC address
    except Exception as ConvertError:
        logging.exception(ConvertError)
        return 201

# Check WakeonLAN address if needed
def AddressFilter(RandomMacAddress, Whitelist=None):
    if Whitelist is not None:
        try:
            # Upper to capital case
            RandomMacAddress = RandomMacAddress.upper()
            # Read JSON storage whitelist
            with open(Whitelist,"r") as CheckReference:
                CheckBook = json.load(CheckReference)
                # Get list
                for ReferenceAddress in CheckBook["AllowAddress"]:
                    # Inside whitelist
                    if RandomMacAddress == ReferenceAddress.upper():
                        CheckReference.close()
                        return RandomMacAddress
                    # Otherwise
                    elif RandomMacAddress != ReferenceAddress.upper():
                        CheckReference.close()
                        return 301
        # Whitelist JSON not found
        except FileNotFoundError:
            return RandomMacAddress
        # Error occurred
        except Exception as FilterError:
            logging.exception(FilterError)
            return 302
    # Disable Whitelist check
    elif Whitelist is None:
        return RandomMacAddress

# Sending WakeonLAN packet
def LocalBroadcasting(WakeupMacAddress, AddressConfig=None, PortConfig=None):
    # Translate MAC address into WoL bytes packet
    WakeUpPacket = AddressTranslatedintoBytes(WakeupMacAddress)
    # Error occurred during translate
    if type(WakeUpPacket) is int:
        return WakeUpPacket
    # Successfully translate into bytes packet
    elif type(WakeUpPacket) is bytes:
        try:
            # IP address config, default
            if AddressConfig is None:
                BroadcastAddress = "255.255.255.255"
            elif AddressConfig is not None:
                BroadcastAddress = AddressConfig
            # Port config, default
            if PortConfig is None:
                BroadcastPort = 9
            elif PortConfig is not None:
                BroadcastPort = PortConfig
            # Broadcast socket config
            BroadcastMission = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            BroadcastMission.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
            BroadcastMission.sendto(WakeUpPacket,(BroadcastAddress,BroadcastPort))
            BroadcastMission.close()
            return WakeupMacAddress
        except Exception as BroadcastingError:
            logging.exception(BroadcastingError)
            return 401

# Forwarding MAC address
def SocketForwarding(ForwardingPayload, ForwardingCheck=None, ForwardingRecord=None, ForwardingAddress=None, ForwardingPort=None):
    # Receiving incorrect data
    if type(ForwardingPayload) is int:
        # Logging incorrect data receiving
        WakeupBooking(RecordFile=ForwardingRecord, AddressLogging=("Omit incorrect data."))
        return int
    # Receiving MAC address
    elif type(ForwardingPayload) is str:
        # Using whitelist
        FilterCheck = AddressFilter(ForwardingPayload, Whitelist=ForwardingCheck)
        # MAC Address match whitelist, or Disable whitelist check
        if type(FilterCheck) is str:
            LocalBroadcasting(FilterCheck, AddressConfig=ForwardingAddress, PortConfig=ForwardingPort)
            # Logging receiving MAC address
            WakeupBooking(RecordFile=ForwardingRecord, AddressLogging=FilterCheck)
            return True
        # Didn't match whitelits, Ignore
        elif type(FilterCheck) is int:
            # Logging unmatch MAC address event
            WakeupBooking(RecordFile=ForwardingRecord, AddressLogging=("Omit unmatch MAC address."))
            return False

# 2024.03.25