import os
from netmiko import Netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from getpass import getpass

user = input('Please enter your username: ')
secret = getpass('Please enter your password: ')

ciscoDevice = {
	'device_type': 'cisco_ios',
	'host': '192.168.154.135',
	'username': user,
	'password': secret

}

try:
	connection = ConnectHandler(**ciscoDevice)
except (NetMikoTimeoutException):
	print('The following device timed out: ' + ciscoDevice['host'])
except (AuthenticationException):
	print('Authentication failure on: ' + ciscoDevice['host'])
except (SSHException):
	print('Could not connect to the device with SSH. Check your SSH setings on: ' + ciscoDevice['host'])
except (EOFError):
	print('End of file while attempting: ' + ciscoDevice['host'])
except Exception as other_error:
	print('The error ' + str(other_error) + ' occurred while connecting to: ' + ciscoDevice['host'])
print('The script has completed')

