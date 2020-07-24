# Python Runnung Wake-on-LAN

[![wol](https://github.takahashi65.info/lib_badge/wake-on-lan.svg)](https://pypi.org/project/wakeonlan/) 
[![python](https://github.takahashi65.info/lib_badge/python.svg)](https://www.python.org/)
[![python version](https://github.takahashi65.info/lib_badge/python-3.6.svg)](https://www.python.org/) 
[![UA](https://github.takahashi65.info/lib_badge/under-development.svg)](https://github.com/Suzhou65/Python-Wake-on-LAN)

**What is this?**<br>
Using Python sending Magic Packet to runnung Wake-on-LAN function, has GUI
![ScreenShot](https://github.takahashi65.info/lib_img/github_wol_success.png)  

![ScreenShot](https://github.takahashi65.info/lib_img/github_wol_sa_success.png)

Command-line interface support
![ScreenShot](https://github.takahashi65.info/lib_img/github_wol_cli.png)

## File Description
**wakeonlan_cli.py** / **wakeonlan_gui.py**  
Python Module "wakeonlan" is required

**wakeonlan_standalone_cli.py** / **wakeonlan_standalone_gui.py**  
Module "wakeonlan" not required

## Working Environments
**Python Module "wakeonlan"**  
Visit Resources link to install module  
Standalone version doesn't need to install module

**Python Version**
Python 3.6.8 or higher

### How Python convert string into bytes
```python
str_mac = '1A-1B-4C-5D-1E-4F'

if len(str_mac) == 17:
    separate = str_mac[2]
    str_mac = str_mac.replace(separate, "")
elif len(str_mac) != 12:
    print("MAC Address Input error")
        
hex_mac = bytes.fromhex("F" * 12 + str_mac *16)
```
  
or
  
```python
str_mac = '1A-1B-4C-5D-1E-4F'

def check_mac():
    global str_mac
    #Trans input mac adress
    if len(str_mac) == 17:
        separate = str_mac[2]
        str_mac = str_mac.replace(separate, "")
        print("MAC Address check complete")
    #If Mac address format incorrect
    elif len(str_mac) != 12:
        print("MAC Address Input error")
    
    #Trans input mac adress into bytes
    return bytes.fromhex("F" * 12 + str_mac *16)

bytes_mac = check_mac()
```

## Resources
- [wakeonlan Module](https://pypi.org/project/wakeonlan/)
- [Python Wake-on-LAN, code example](https://github.com/remcohaszing/pywakeonlan)