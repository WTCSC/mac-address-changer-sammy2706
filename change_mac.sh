#!/bin/bash
# If user types in an invalid command, then this prompt will pop up to guide them
Usage()
{
    echo "Usage: $0 -i <interface> -m <MAC address>"
    echo
    echo "Options:"
    echo "  -i    Network interface (e.g., eth0, wlan0)"
    echo "  -m    New MAC address in the format A1:B4:C5:C1:DD:3E"
    echo
    echo "Examples:"
    echo "  $0 -i eth0 -m A1:B4:C5:C1:DD:3E"
    echo "  $0 -i wlan0 -m 00:11:22:33:44:55"
    echo
    exit 1

}

checker()
{
    if [[ "$1" =~ ^[A-F0-9]{2}(:[A-F0-9]{2}){5}$ ]]; then # This function validates the MAC address fromat using regex patterns
        return 0
    else
        return 1
    fi
}
while getopts ":i:m:" OPTION; do
    case $OPTION in
        i) 
            IP="$OPTARG";; # Assigns the network interface value to the variable IP.
        m)
            MAC="$OPTARG" # Assigns the MAC address value to the variable MAC
            if ! checker "$MAC"; then # Validates the MAC address format
                Usage
            fi
            ;;
            
        *) 
            Usage;;
    
    esac
done

shift $(($OPTIND - 1))

# Checks if the variables are set, if not, the usage instructions pop up
if [ -z "$IP" ]; then
    Usage
fi
if [ -z "$MAC" ]; then
    Usage
fi


sudo ifconfig $IP down # Brings the netwrok interface down
sudo ifconfig $IP hw ether $MAC # Sets the new MAC address
sudo ifconfig $IP up # Brings the network interface back up