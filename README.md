# Python Running Wake-on-LAN
[![wol](https://github.takahashi65.info/lib_badge/wake-on-lan.svg)](https://pypi.org/project/wakeonlan/) 
[![python version](https://github.takahashi65.info/lib_badge/python-3.6.svg)](https://www.python.org/) 
[![php](https://github.takahashi65.info/lib_badge/php-7.3.0.svg)](https://www.php.net/) 
[![UA](https://github.takahashi65.info/lib_badge/active_maintenance.svg)](https://github.com/Suzhou65/Python-Wake-on-LAN)
[![Size](https://github-size-badge.herokuapp.com/Suzhou65/Python-Wake-on-LAN.svg)](https://github.com/axetroy/github-size-badge)

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
    + [Wake-on-LAN CLI](#wake-on-lan-cli)
    + [Wake-on-LAN GUI](#wake-on-lan-gui)
    + [Wake-on-LAN Forwarding](#wake-on-lan-forwarding)
    + [Wake-on-LAN Forwarding Nolog](#wake-on-lan-forwarding-nolog)
    + [Wake-on-LAN Status](#wake-on-lan-status)
  * [Dependencies](#dependencies)
    + [Python version](#python-version)
    + [Python module](#python-module)
    + [Apache HTTP Server](#apache-http-server)
  * [License](#license)
  * [Resources](#resources)

## Usage
### Port Forwarding
You need to setting router port forwarding function, set **Port 9 | UDP** forward to the device you running Magic Packet forwarding program. Port 9 is the defult port number sending and receiving Magic Packet, but sometimes you need to switch it due to some limited.

### Root Privileges
TCP/UDP ports below 1024 are privileged, so bind socket below 1024 need root privileges. If you didn't using sudo command, you will see the alert message likes below.
```text
2020-08-13 17:21:57 | Ports below 1024 are privileged, require root privileges !
```
If you dont't have root privileges, or cannot using sudo command, please switch the **receive_protocol** port over 1024. For example:
```python
try:
  # Get Host
  receive_host = wakeonlan.host_info()
  # Listening socket config
  receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
  receive_protocol = 9
  receive_socket.bind((receive_host, receive_protocol))
  # If ports below 1024 require root privileges
except PermissionError:
  print(f"{time_start} | Ports below 1024 are privileged, require root privileges !")
  sys.exit(0)
```
### Terminal multiplexer
[GNU Screen](https://www.gnu.org/software/screen/) is recommended, it can let you running Magic Packet forwarding program at background.

### Port Forwarding Status Monitor
Apache HTTP Server, and php 7.3 is necessary, after install, you need to enable php function at Apache.
```shell
sudo apt install php
sudo apt install libapache2-mod-php7.3
sudo a2enmod php7.3
sudo systemctl restart apache2
```

**wakeonlan_status.php** is a simple monitoring web page, **it didn't have any secure protection**. If you value you MAC address as personal privacy, please running it on LAN network environments only, or added some protection function, [see the example GitHub Gist](https://gist.github.com/Suzhou65/eed12200e516aac88b83f8ee6ec3dc7a).

## Import module
- Import as module
```
import wakeonlan
```

## Function
### Wake-on-LAN CLI
Command-line interface version.
```shell
pi@raspberrypi:~/python_script $ python wakeonlan_script_cli.py
```
```text
2020-08-13 17:22:52 | Python wakeonlan
Enter MAC Address: 2A-61-C8-B1-5E-46
Enter IP Address ( Default is Broadcast ) : 192.168.0.5
```
It will sending magic packet, and printing:
```text
2020-08-13 17:22:57 | Magic Packet Sending ...
```
If set as broadcasting, it will printing:
```text
2020-08-13 17:23:05 | Magic Packet Broadcasting ...
```

### Wake-on-LAN GUI
Graphical User Interface version.
```shell
pi@raspberrypi:~/python_script $ python wakeonlan_script_gui.py
```
It will pop up a graphical user interface windows.

### Wake-on-LAN Forwarding
Forwarding Magic Packet and broadcasting.
```shell
pi@raspberrypi:~/python_script $ python wakeonlan_forwarding.py
```
If initialize successfully, it will print this:
```text
2020-08-13 17:22:52 | Initialize complete. Record file create
2020-08-13 17:22:52 | Now monitoring 10.0.1.2, pressing CTRL+C to exit
```
Now it will monitoring the network, and forwarding Magic Packet by broadcasting, it also record the receiving data.

If you want to terminate the Program, pressing CTRL+C, it will print this:
```
^C
2020-08-13 17:23:28 | Thank you for using the Wakeup forwarding.
GoodBye ...
```
The receiving Magic Packet will be translate into MAC address, recording as CSV file with receiving time. The file also recording program start / terminate time, and error occurred time when receiving incomplete packet.

For example:
```csv
stamp,address

2020-11-10 12:08:39,70-a7-af-3d-17-c5
2020-12-24 14:29:08,5b-0c-f1-c1-4c-b0
2020-12-25 15:36:46,Omit
2020-12-28 11:06:24,70-a7-af-3d-17-c5
2021-01-09 21:27:29,Omit
2021-01-11 14:40:34,5b-0c-f1-c1-4c-b0
2021-01-18 19:45:58,Omit Reveille
```

You can also setting ```Ignore wakeup all``` configuration, this configuration is inside the forwarding script.
```python
# Ignore wakeup all
ignroe_reveille = True
```

### Wake-on-LAN Forwarding Nolog
Forwarding Magic Packet and broadcasting.
```shell
pi@raspberrypi:~/python_script $ python wakeonlan_forwarding_nolog.py
```
Same function as previous python script, but this one won't generated any record file, it won't logging.

You can also setting ```Ignore wakeup all``` configuration, this configuration is inside the forwarding script.
```python
# Ignore wakeup all
ignroe_reveille = True
```


### Wake-on-LAN Status
View Magic Packet Magic forwarding status on web browser.
```php
<!-- php block -->
<?php
  // File path as you python script location
  if ($file = fopen("/python_script_location/wakeup_record.csv","r")){
    while (($line = fgetcsv($file)) !== false){
      echo "<tr>";
      foreach ($line as $cell) {echo "<td>" . htmlspecialchars($cell) . "</td>";}
      echo "</tr>\n";}
      fclose($file);
```
File path depend on you python script location.

## Dependencies
### Python version
- Python 3.6 or above

### Python module
- sys
- csv
- datetime
- socket
- tkinter

### Apache HTTP Server
- apache2, verson 2.4.46 or above
- php 7.3 or above

## License
General Public License -3.0

## Resources
- [wakeonlan Module](https://pypi.org/project/wakeonlan/)
- [Python Wake-on-LAN, code example](https://github.com/remcohaszing/pywakeonlan)
