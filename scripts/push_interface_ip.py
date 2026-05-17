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
