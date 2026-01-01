import socket # Import the socket module to work with network interfaces
import uuid # Import the uuid module to get MAC address
import subprocess # Import the subprocess module to run system commands
from datetime import datetime # Import datetime module to work with date and time
import platform # Import platform module to get system information

def menu():
    print("\n--------Network Information Menu--------")
    print("1. Show Hostname and IP Address")
    print("2. Show MAC Address")
    print("3. Show Network Interfaces")
    print("4. Ping Test")
    print("5. DNS Lookup")
    print("6. Exit & Save Report")

def get_network_interfaces():
   hostname = socket.gethostname()
   try:
       ip_address = socket.gethostbyname(hostname)
   except socket.gaierror:
       ip_address = "Unable to get IP address"
   return hostname, ip_address

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    return mac_address

def dns_lookup():
    host = input("Enter hostname for DNS lookup (ex: google.com): ")
    try:
        ip_address = socket.gethostbyname(host)
        print(f"IP Address of {host}: {ip_address}")
    except socket.gaierror:
        print("DNS lookup failed. Hostname not found.")

def port_scan():
    host = input("Enter host to scan (ex: google.com): ")
    try:
        ip_address = socket.gethostbyname(host)
        print(f"Starting port scan on {host} ({ip_address})...")
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
    except socket.gaierror:
        print("Port scan failed. Hostname not found.")

def print_network_info():
    hostname, ip_address = get_network_interfaces()
    mac_address = get_mac_address()
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"MAC Address: {mac_address}")

def get_interface():
    system = platform.system()
    interfaces = []
    try:
        if system == "Windows":
            output = subprocess.check_output("ipconfig", shell=True).decode()
            interfaces = output.split("\n")
        else:
            output = subprocess.check_output("ifconfig", shell=True).decode()
            interfaces = output.split("\n")
    except Exception as e:
        interfaces.append(f"Error retrieving interfaces: {e}")
    return interfaces  

def ping_test():
    host = input("Enter host to ping (ex: google.com): ")
    try:
        output = subprocess.check_output(
            f"ping -c 4 {host}", shell=True
        ).decode()
        print(output)
    except subprocess.CalledProcessError:
        print("Ping failed. Host unreachable.")


def save_file():
    hostname, ip_address = get_network_interfaces()
    mac_address = get_mac_address()
    interfaces = get_interface()
    filename = f"network_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open("network_info.txt", "w") as f:
        f.write(f"Hostname: {hostname}\n")
        f.write(f"IP Address: {ip_address}\n")
        f.write(f"MAC Address: {mac_address}\n")
        f.write("Network Interfaces:\n")
        for interface in interfaces:
            f.write(f"{interface}\n")
    print("Network information saved to network_info.txt")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            print_network_info()
        elif choice == '2':
            mac_address = get_mac_address()
            print(f"MAC Address: {mac_address}")
        elif choice == '3':
            interfaces = get_interface()
            print("Network Interfaces:")
            for interface in interfaces:
                print(interface)
        elif choice == '4':
            ping_test()
        elif choice == '5':
            dns_lookup()
        elif choice == '6':
            save_file()
            print("Exiting the program....")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()