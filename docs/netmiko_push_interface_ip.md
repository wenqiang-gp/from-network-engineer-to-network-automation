# Using Netmiko to Push Interface IP Configuration

## Lab Topology
![Operate and observe the arrival log through Eve's simulation console interface Topology](topology/Operate and observe the arrival log through Eve's simulation console interface.png)

## Device Information
- Cisco IOS
- SSH enabled

## Goal
Use Python + Netmiko to configure interface IP automatically.

## Python Script
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.66.130",
    "username": "admin",
    "password": "Admin@123",
}

commands = [
    "interface e0/1",
    "ip address 192.168.10.1 255.255.255.0",
    "no shutdown",
    "interface e0/2",
    "ip address 192.168.20.1 255.255.255.0",
    "no shutdown",
]

with ConnectHandler(**device) as conn:
    output = conn.send_config_set(commands)
    print(output)

## Result
![Successfully configured the simulated router of EVE using Python in Ubuntu Topology](topology/Successfully configured the simulated router of EVE using Python in Ubuntu.png)
