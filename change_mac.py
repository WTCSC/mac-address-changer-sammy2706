import sys
import re
import subprocess
import argparse

# Fucntion to display usage instructions
def usage():
    print("Usage: python3 <interface> <new_mac>")
    print()
    print("Options:")
    print("-i    Network interface (e.g., eth0, wlan0)")
    print("-m    New MAC address in the format A1:B4:C5:C1:DD:3E")
    print()
    print("Examples:")
    print("python3 -i eth0 -m A1:B4:C5:C1:DD:3E")
    print("python3 -i wlan0 -m 00:11:22:33:44:55")
    print()
    sys.exit(1)

# Fucntion to validate MAC address using regural expressions
def validate_mac(mac):
    if re.match(r"[A-F0-9]{2}(:[A-F0-9]{2}){5}$", mac, re.I):
        return True
    else:
        return False

# Function to change MAC address of a network interface
def change_mac(I , new_mac_address):
    subprocess.run(["sudo", "ifconfig", I, "down"])
    subprocess.run(["sudo", "ifconfig", I, "hw", "ether", new_mac_address])
    subprocess.run(["sudo", "ifconfig", I, "up"])

# Function to parse command line arguments
def main():
    parser = argparse.ArgumentParser(description="Change MAC address of a network interface")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address in the format A1:B4:C5:C1:DD:3E")

    # Checks if the user has entered any arguments
    if len(sys.argv) == 1:
        usage() # Displays usage instructions
    
    try:
        args = parser.parse_args()
    except argparse.ArugumentError:
        usage()

    # Validates the given mac address
    if not validate_mac(args.mac):
        print("Invalid MAC address")
        usage()

    change_mac(args.interface, args.mac)

if __name__ == "__main__":
    main()