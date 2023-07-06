from getpass import getpass
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.exceptions import NetmikoAuthenticationException


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
except (NetmikoTimeoutException):
	print('The following device timed out: ' + ciscoDevice['host'])
except (NetmikoAuthenticationException):
	print('Authentication failure on: ' + ciscoDevice['host'])
except (SSHException):
	print('Could not connect to the device with SSH. Check your SSH setings on: ' + ciscoDevice['host'])
except (EOFError):
	print('End of file while attempting: ' + ciscoDevice['host'])
except Exception as other_error:
	print('The error ' + str(other_error) + ' occurred while connecting to: ' + ciscoDevice['host'])
print('The script has completed')

