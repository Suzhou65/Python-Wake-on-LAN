# Python Running Wake-on-LAN
[![wol](https://github.takahashi65.info/lib_badge/wake-on-lan.svg)](https://pypi.org/project/wakeonlan/)
[![python version](https://github.takahashi65.info/lib_badge/python-3.9.svg)](https://www.python.org/) 
[![php](https://github.takahashi65.info/lib_badge/php-8.3.0.svg)](https://www.php.net/) 
[![UA](https://github.takahashi65.info/lib_badge/active_maintenance.svg)](https://github.com/Suzhou65/Python-Wake-on-LAN)
[![Size](https://img.shields.io/github/repo-size/Suzhou65/Python-Wake-on-LAN)](https://shields.io/category/size)

Using Python sending Magic Packet, or forwarding it.

## Contents
- [Python Running Wake-on-LAN](#python-running-wake-on-lan)
  * [Contents](#contents)
  * [Usage](#usage)
    + [Port Forwarding](#port-forwarding)
    + [Root Privileges](#root-privileges)
    + [Terminal multiplexer](#terminal-multiplexer)
    + [Port Forwarding Status Monitor](#port-forwarding-status-monitor)
  * [Import module](#import-module)
  * [Function](#function)
    + [Wake-on-LAN Script](#wake-on-lan-script)
    + [Wake-on-LAN Forwarding](#wake-on-lan-forwarding)
    + [Forwarding Status](#forwarding-status)
  * [Dependencies](#dependencies)
    + [Python version](#python-version)
    + [Python module](#python-module)
    + [Apache HTTP Server](#apache-http-server)
  * [License](#license)
  * [Resources](#resources)

## Usage
### Port Forwarding
You need to setting router port forwarding function, set **UDP, Port 9** forward to the device you running Magic Packet forwarding program. Port 9 is the defult port number sending and receiving Magic Packet, but sometimes you need to switch it due to some limited.
### Root Privileges
TCP/UDP ports below 1024 are privileged, so bind socket below 1024 need root privileges. If you didn't using sudo command, you will see the alert message likes below.
```python
# Ports below 1024 require root privileges
except PermissionError:
    PermissionMessage = ("Ports below 1024 are privileged, require root privilege.")
    wakeonlan.StatusBooking(StatusFile=StatusPath,StatusLogging=PermissionMessage)
    print(f"{PermissionMessage}\r\n")
```
If you dont't have root privileges, or cannot using sudo command, please switch the **HostProtocol** port over 1024. For example:
```python
# Get host info
HostAddress = wakeonlan.NetEnvkCheck()
# Socket configuration
ListeningSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HostProtocol = 7
ListeningSocket.bind((HostAddress,HostProtocol))
```
### Terminal multiplexer
[GNU Screen](https://www.gnu.org/software/screen/) is recommended, it can let you running Magic Packet forwarding program at background.
### Port Forwarding Status Monitor
Apache HTTP Server, and php 7.3 is necessary, after install, you need to enable php function at Apache.
```shell
sudo apt install php8.3 
sudo apt install php8.3-fpm
sudo a2enmod proxy_fcgi setenvif
sudo a2dismod php8.3
sudo a2enconf php8.3-fpm
sudo systemctl restart apache2
```

## Import module
- Import as module
```
import wakeonlan
```

## Function
### Wake-on-LAN Script
Switch between CLI mode or GUI mode.
```python
# GUI mode switch
EnableGUI = False
```
Set ```True``` It will pop up a graphical user interface windows.
### Wake-on-LAN Forwarding
Forwarding Magic Packet and broadcasting.
```shell
root@host:~/script_local $ sudo python wakeonlan_forwarding.py
```
Following message will display.
```
Now monitoring address: 192.168.1.2
Port number: 7

Pressing Ctrl+C to exit.
```
Now it will monitoring the network, and forwarding Magic Packet by broadcasting, it also record the receiving data.

If you want to terminate the Program, pressing CTRL+C, it will print this:
```
Script has been manually stopped.
```
The receiving Magic Packet will be translate into MAC address, recording as CSV file with receiving time. The file also recording program start / terminate time, and error occurred time when receiving incomplete packet.

You can also setting ```MAC addrsss whitelist``` configuration, this configuration is inside the script.
```python
# Whitelist path, To disable function, set into None
FilterPath = "/file_path/wakeonlan.whitelist.json"
```
Please editing the whitelist file named ```wakeonlan.whitelist.json```.
```json
{
  "AllowAddress":[
    "FF:FF:FF:FF:FF:FF",
    "",
    ""
    ],
  "Comment":[
    "USE CAPITAL CASE",
    "IF YOU ALLOW WAKEUP ALL, ADD FF:FF:FF:FF:FF:FF INTO AllowAddress LIST"
    ]
}
```
### Forwarding Status

## Dependencies
### Python version
- Python 3.9 or above
### Python module
- csv
- sys
- json
- socket
- logging
- datetime
### Apache HTTP Server
- Apache or NGINX
- php 8.3 or above, recommend using php-FPM

## License
General Public License -3.0

## Resources
- [wakeonlan Module](https://pypi.org/project/wakeonlan/)
- [Python Wake-on-LAN, code example](https://github.com/remcohaszing/pywakeonlan)
