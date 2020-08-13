# Python Running Wake-on-LAN

[![wol](https://github.takahashi65.info/lib_badge/wake-on-lan.svg)](https://pypi.org/project/wakeonlan/) 
[![python](https://github.takahashi65.info/lib_badge/python.svg)](https://www.python.org/)
[![python version](https://github.takahashi65.info/lib_badge/python-3.6.svg)](https://www.python.org/) 
[![UA](https://github.takahashi65.info/lib_badge/raspberry-pi.svg)](https://www.raspberrypi.org/)
[![UA](https://github.takahashi65.info/lib_badge/active_maintenance.svg)](https://github.com/Suzhou65/Python-Wake-on-LAN)

**What is this?**<br>
Using Python sending Magic Packet, or forwarding it.
![ScreenShot](https://github.takahashi65.info/lib_img/github_wol_sa_success.png)

![ScreenShot](https://github.takahashi65.info/lib_img/github_wakeonlan_status.png)
## File Description
**PyPI_wakeonlan_cli.py** / **SA_wakeonlan_cli.py**  
Command-line interface version.
![ScreenShot](https://github.takahashi65.info/lib_img/github_wol_cli.png)

**PyPI_wakeonlan_gui.py** / **SA_wakeonlan_gui.py**  
Graphical User Interface version.
![ScreenShot](https://github.takahashi65.info/lib_img/github_wol_success.png)

**wakeonlan_forward.py**  
Forwarding Magic Packet and broadcasting, it also record the receiving data.
![ScreenShot](https://github.takahashi65.info/lib_img/github_wakeonlan_root.png)

![ScreenShot](https://github.takahashi65.info/lib_img/github_wakeonlan_record.png)

## Attention
**Port Forwarding**  
You need to setting router port forwarding function, set **Port 9 | UDP** forward to the device you running **wakeonlan_forward.py**. Port 9 is the defult port number sending and receiving Magic Packet, but sometimes you need to switch it, seen the description below.

**Root Privileges**  
TCP/UDP ports below 1024 are privileged, so bind socket below 1024 need root privileges. If you didn't using sudo command, you will see the alert message likes below.
![ScreenShot](https://github.takahashi65.info/lib_img/github_wakeonlan_forward.png)

If you dont't have root privileges, or cannot using sudo command, please switch the **receive_protocol** port over 1024. For example:
```python
try:
    #Print when ready to go
    receive_protocol = 1080
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    receive_socket.bind((receive_host, receive_protocol))
    print (f"{time_start} | Monitoring {receive_host}")
```

## Working Environments
**Python Module "wakeonlan"**  
Visit Resources link to install module, standalone version (SA) doesn't need to install module.

**Python Version**  
Due to **f-string** function support version is 3.6 or higher.

**Terminal multiplexer**  
[GNU Screen](https://www.gnu.org/software/screen/) is recommended, it can let you running Magic Packet forwarding program at background.

## Resources
- [wakeonlan Module](https://pypi.org/project/wakeonlan/)
- [Python Wake-on-LAN, code example](https://github.com/remcohaszing/pywakeonlan)