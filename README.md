# Python Running Wake-on-LAN
[![wol](https://github.takahashi65.info/lib_badge/wake-on-lan.svg)](https://pypi.org/project/wakeonlan/)
[![python](https://github.takahashi65.info/lib_badge/python.svg)](https://www.python.org/) 
[![php](https://github.takahashi65.info/lib_badge/php-7.3.0.svg)](https://www.php.net/) 
[![UA](https://github.takahashi65.info/lib_badge/active_maintenance.svg)](https://github.com/Suzhou65/Python-Wake-on-LAN)
[![Size](https://img.shields.io/github/repo-size/Suzhou65/Python-Wake-on-LAN)](https://shields.io/category/size)

Using Python sending Magic Packet, or forwarding it.

## Contents
- [Python Running Wake-on-LAN](#python-running-wake-on-lan)
  * [Contents](#contents)
  * [Usage](#usage)
    + [Port Forwarding](#port-forwarding)
    + [Root Privileges](#root-privileges)
    + [Troubleshooting](#troubleshooting)
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
You need to setting router port forwarding function, set **UDP 9** forward to the device you running Magic Packet forwarding program. Port number 9 is the defult port number sending and receiving Magic Packet, but sometimes you need to switch it due to some limited.

Forwarding configuration can been found in script ``` wakeonlan_forwarding.py```.
```python
# Forwarding target, Default is 255.255.255.255
Address = None
# Forwarding output port number, Default is port 9
Port = None
```
### Root Privileges
TCP/UDP ports below 1024 are privileged, so bind socket below 1024 need root privileges. If you didn't using sudo command, you will see the alert message likes below.
```
Ports below 1024 are privileged, require root privilege.
```
If you dont't have root privileges, or cannot using sudo command, please switch the **HostProtocol** port over 1024 inside script ```wakeonlan_forwarding.py```.
```python
# Get host info
HostAddress = wakeonlan.NetEnvkCheck()
# Socket configuration
ListeningSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HostProtocol = 7
ListeningSocket.bind((HostAddress,HostProtocol))
```
### Troubleshooting
If forwarding script wasn't stopped normally, you may see the error message at next start up:
```
[Errno 98] Address already in use
```
This error cause by forwarding script wasn't stopped, the socket used by script not release. Please check the task manager:
```shell
ps -fA | grep python
```
Then kill the forwarding script still alive.
### Terminal multiplexer
[GNU Screen](https://www.gnu.org/software/screen/) is recommended, it can let you running Magic Packet forwarding program at background.
### Port Forwarding Status Monitor
Apache HTTP Server, and php 7.3 is necessary, after install, you need to enable php function at Apache.

## Import module
- Import as module
```
import wakeonlan
```

## Function
### Wake-on-LAN Script
Sending Magic Packet.
```shell
root@host:~/script_local $ sudo python wakeonlan_script.py
```
Switch between CLI mode and GUI mode. Set ```True``` It will pop up a graphical user interface windows.
```python
# GUI mode switch
EnableGUI = False
```
Configure default MAC address.
```python
# Default MAC address
DefaultAddress = "FF:FF:FF:FF:FF:FF"
```
### Wake-on-LAN Forwarding
Forwarding Magic Packet and broadcasting to local network environment.
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

If you want to terminate the Program, pressing CTRL+C, it will print:
```
Script has been manually stopped.
```
The receiving Magic packet will be translate into MAC address, recording as CSV file named ```wakeonlan.mac_address.csv``` with receiving time. To disable receiving record, please setting ```RecordPath``` into ```None```.
```python
# MAC address input recoed
RecordPath = "/file_path/wakeonlan.mac_address.csv"
```
Same as script's process status.
```python
# Program status file and path
StatusPath = "/file_path/wakeonlan.forward_status.csv"
```
You can also configure ```MAC addrsss whitelist``` inside script.
```python
# Whitelist path
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
    "IF YOU ALLOW WAKEUP ALL, ADDING FF:FF:FF:FF:FF:FF INTO AllowAddress LIST"
    ]
}
```
Setting ```FilterPath``` into ```None``` will disable whitelist function.
### Forwarding Status
Monitoring the forwarding script by ```wakeonlan_status.php```, please deploy the as normal webpage. Status file locate configuration at ```wakeonlan_status.php``` line 87:
```php
if ($file = fopen("/file_path/wakeonlan.forward_status.csv","r"))
```
MAC address forwarding record at line 106:
```php
if ($file = fopen("/file_path/wakeonlan.mac_address.csv","r"))
```
Password strong as hash, pleae using this script to generate hash.
```php
<?php
  // Input raw password
  $password_input = "Input_Your_Password_Here";
  // Using PASSWORD_DEFAULT for safety
  $hash = password_hash($password_input,PASSWORD_DEFAULT);
  // Print the generated hash
  echo $hash;
?>
```
Copy and paste the hash at ```wakeonlan_status.php``` line 77:
```php
$hash = '$Put_Your_Hashed_Password_at_Here';
```
You can see [demonstration](https://www.takahashi65.info/page/status_wakeonlan.php), password is ```OpenSourceisGreat```.

## Dependencies
### Operating system
- Linux distros.
- For example: Debian, Ubuntu, Fedora, Raspberry Pi OS
### Python version
- Python 3.7.3 or above
- Testing on the above Python version: 3.9.6 / 3.12.2
### Python module
- csv
- sys
- json
- socket
- tkinter
- logging
- datetime
### Apache HTTP Server
- Apache or NGINX
- php 7.3 or above, recommend using php-FPM

## License
General Public License -3.0

## Resources
- [wakeonlan Module](https://pypi.org/project/wakeonlan/)
- [Python Wake-on-LAN, code example](https://github.com/remcohaszing/pywakeonlan)
