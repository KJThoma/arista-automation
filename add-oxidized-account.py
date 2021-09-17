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

arista_3 = {
    'device_type': 'arista_eos',
    'ip': 'your_ip',
    'username': 'your_username',
    'password': 'your_password',
    'session_log': 'sw3.txt'
}

# command to run on switches
commands = ['username oxidized privilege 15 role network-operator secret sha512 <secret>']

# for loop to connect to devices in enabled mode, run on switches, write config, and print output
for device in (arista_1, arista_2, arista_3):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()
    print()
    print('#' * 70)
    print(output)
    print('#' * 70)
    print()
