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
def RecordFileInitialize(RecordFilePath=(),StatusFilePath=()):
    if bool(RecordFilePath) is True:
        try:
            CheckRecordFile = open(RecordFilePath,mode="r")
            CheckRecordFile.close()
        except FileNotFoundError:
            with open(RecordFilePath,mode="w",newline="") as RecordTapeInitialize:
                RecordTape = csv.writer(RecordTapeInitialize, delimiter=",")
                RecordTape.writerow(["Time","Address"])
                RecordTapeInitialize.close()
    elif bool(RecordFilePath) is False:
        pass
    if bool(StatusFilePath) is True:
        try:
            CheckStatusFile = open(StatusFilePath,mode="r")
            CheckStatusFile.close()
        except FileNotFoundError:
            with open(StatusFilePath,mode="w",newline="") as StatusTapeInitialize:
                StatusTape = csv.writer(StatusTapeInitialize,delimiter=",")
                CreateStatusTapeTime = GetTime()
                StatusTape.writerow([CreateStatusTapeTime,"Initialization complete"])
                StatusTapeInitialize.close()
    elif bool(StatusFilePath) is False:
        pass

# Check whitelist file
def WhitelistInitialize(WhitelistPath):
    try:
        with open(WhitelistPath,"r") as WhitelistCheck:
                WhitelistCheck.close()
    except FileNotFoundError:
        # Dictionary
        WhitelistDict = {
            "AllowAddress":[
                "",
                "",
                "",
                "",
                ""],
            "Comment":[
                "USE CAPITAL CASE",
                "IF YOU ALLOW WAKEUP ALL, ADD FF:FF:FF:FF:FF:FF INTO AllowAddress LIST"]
                }
        # Save
        with open(WhitelistPath,"w") as WhitelistCreate:
            json.dump(WhitelistDict,WhitelistCreate,indent=2)
            WhitelistCreate.close()

# Typing MAC address accepted
def AddressBooking(RecordFilePath,AddressLogging):
    try:
        AddressBookingTime = GetTime()
        AddressBookingRow = [AddressBookingTime,AddressLogging]
        # Writing to MAC address record
        with open(RecordFilePath,mode="a",newline="") as AddressBook:
            AddressTape = csv.writer(AddressBook,delimiter=",")
            AddressTape.writerow(AddressBookingRow)
            AddressBook.flush()
            AddressBook.close()
        return AddressBookingRow
    except Exception as BookingError:
        logging.exception(BookingError)
        pass

# Program executive logging
def StatusBooking(StatusFilePath,StatusLogging=()):
    try:
        StatusBookingTime = GetTime()
        StatusBookingRow = [StatusBookingTime,StatusLogging]
        # Writing status record
        with open(StatusFilePath,mode="w",newline="") as StatusBook:
            StatusTape = csv.writer(StatusBook, delimiter=",")
            StatusTape.writerow(StatusBookingRow)
            StatusBook.close()
            return StatusBookingRow
    except Exception as BookingError:
        logging.exception(BookingError)
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
def Address2Packet(MacAddress):
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
            return False
    except Exception as ConvertError:
        logging.exception(ConvertError)
        return False

# Convert bytes to MAC address
def Packet2Address(PacketInput):
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
        return False

# Check WakeonLAN address if needed
def AddressFilter(WhitelistPath,RandomMacAddress):
    try:
        # Upper to capital case
        RandomMacAddress = RandomMacAddress.upper()
        # Read JSON storage whitelist
        with open(WhitelistPath,"r") as CheckReference:
            CheckBook = json.load(CheckReference)
            # Get list
            for ReferenceAddress in CheckBook["AllowAddress"]:
                # Inside whitelist
                if RandomMacAddress == ReferenceAddress.upper():
                    return RandomMacAddress
                # Otherwise
                elif RandomMacAddress != ReferenceAddress.upper():
                    return 401
    # Whitelist JSON not found
    except FileNotFoundError:
        return RandomMacAddress
    except Exception as FilterError:
        logging.exception(FilterError)
        return False

# Sending WakeonLAN packet
def LocalBroadcasting(PacketPayload,SelectAddress=(),SelectProtocolNumber=()):
    try:
        # IP address config
        if bool(SelectAddress) is False:
            SelectAddress = "255.255.255.255"
        elif bool(SelectAddress) is True:
            pass
        # Port config
        if bool(SelectProtocolNumber) is False:
            SelectProtocolNumber = 9
        elif bool(SelectProtocolNumber) is True:
            pass
        # Broadcast socket config
        BroadcastMission = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        BroadcastMission.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
        BroadcastMission.sendto(PacketPayload,(SelectAddress,SelectProtocolNumber))
        BroadcastMission.close()
        return PacketPayload
    except Exception as BroadcastingError:
        logging.exception(BroadcastingError)
        return False

# Forwarding MAC address
def SocketForwarding(AddressInput,WhitelistPath=(),RecordFilePath=(),SelectAddress=(),SelectProtocolNumber=()):
    # Receiving incorrect data
    if type(AddressInput) is bool:
        AddressLogging=("Omit incorrect data")
        # Logging incorrect data receiving
        if bool(RecordFilePath) is True:
            AddressBooking(RecordFilePath,AddressLogging)
            return(RecordFilePath,AddressLogging)
        # Ignore logging
        elif bool(RecordFilePath) is False:
            return(AddressLogging)
    # Receiving MAC address, Using whitelist
    elif type(AddressInput) is str and bool(WhitelistPath) is True:
        # Check MAC address by filter
        FilterCheck = AddressFilter(WhitelistPath,AddressInput)
        # MAC Address match whitelist
        if type(FilterCheck) is str:
            # Translate address into WoL packet
            PacketPayload = Address2Packet(FilterCheck)
            # Broadcasting
            LocalBroadcasting(PacketPayload,SelectAddress,SelectProtocolNumber)
            # Logging receiving MAC address
            if bool(RecordFilePath) is True:
                AddressBooking(RecordFilePath,AddressInput)
                return(RecordFilePath,WhitelistPath,AddressInput)
            # Ignore logging
            elif bool(RecordFilePath) is False:
                return(WhitelistPath,AddressInput)
        # Didn't match whitelits, Ignore
        elif type(FilterCheck) is int:
            return False
    # Receiving MAC address, broadcasting without whitelist check
    elif type(AddressInput) is str and bool(WhitelistPath) is False:
        # Translate address into WoL packet
        PacketPayload = Address2Packet(AddressInput)
        # Broadcasting
        LocalBroadcasting(PacketPayload,SelectAddress,SelectProtocolNumber)
        # Logging receiving MAC address
        if bool(RecordFilePath) is True:
            AddressBooking(RecordFilePath,AddressInput)
            return(RecordFilePath,AddressInput)
        # Ignore logging
        elif bool(RecordFilePath) is False:
            return (AddressInput)

# 2024.03.24