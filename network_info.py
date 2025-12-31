import socket # Import the socket module to work with network interfaces
import uuid # Import the uuid module to get MAC address
import subprocess # Import the subprocess module to run system commands

def menu():
    print("\n--------Network Information Menu--------")
    print("1. Show Hostname and IP Address")
    print("2. Show MAC Address")
    print("3. Show Network Interfaces")
    print("4. Exit")

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

def get_interface():
    interfaces = subprocess.check_output("ip -br link", shell=True).decode().strip().split('\n')
    return interfaces

def save_file():
    hostname, ip_address = get_network_interfaces()
    mac_address = get_mac_address()
    interfaces = get_interface()
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
            save_file()
            print("Exiting the program....")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()