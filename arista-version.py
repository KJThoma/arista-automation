from netmiko import ConnectHandler

# our device
arista_EOS = {
    'device_type': 'arista_eos',
    'ip': 'your_ip',
    'username': 'your_username',
    'password': 'your_password'
}

# define connection
net_connect = ConnectHandler(**arista_EOS)

# send show version command and nicely print output
output = net_connect.send_command('show version')
print()
print('#' * 70)
print(output)
print('#' * 70)
print()

# gracefully end connection
net_connect.disconnect()

