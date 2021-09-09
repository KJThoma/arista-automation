from netmiko import ConnectHandler

# our devices info to connect and session log files to save output
arista_1 = {
    'device_type': 'arista_eos',
    'ip': 'your_ip',
    'username': 'your_username',
    'password': 'your_password',
    'session_log': 'sw1.txt'
}

arista_2 = {
    'device_type': 'arista_eos',
    'ip': 'your_ip',
    'username': 'your_username',
    'password': 'your_password',
    'session_log': 'sw2.txt'
}

# command to run on switches
command = "show version"

# for loop to connect to devices, run on both switches, and print output
for device in (arista_1, arista_2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(command)
    print()
    print('#' * 70)
    print(output)
    print('#' * 70)
    print()

# gracefully end connection
net_connect.disconnect()

