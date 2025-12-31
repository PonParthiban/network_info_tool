import socket # Import the socket module to work with network interfaces
import uuid # Import the uuid module to get MAC address
import subprocess # Import the subprocess module to run system commands

def get_network_interfaces():
   hostname = socket.gethostname()
   ip_address = socket.gethostbyname(hostname)
   return hostname, ip_address

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    return mac_address

def print_network_info():
    hostname, ip_address = get_network_interfaces()
    mac_address = get_mac_address()
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"MAC Address: {mac_address}")

print_network_info()

print("\nNetwork interfaces:")
output = subprocess.check_output("ip -br  link", shell=True).decode()
print(output)