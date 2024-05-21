import subprocess
import pyfiglet

class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

text = pyfiglet.figlet_format("Ip_Changer")
print(Color.RED,text)
def ip_changer():
    try:
        interface = input(Color.YELLOW + "Enter Your Interface = ")
        ip = input("Enter ip Address = ")
        netmask = input("Enter Netmask = ")

        subprocess.call(["sudo","ifconfig", interface, ip, "netmask", netmask])
        print(Color.BLUE + "Your Ip Address is Changed")
    except KeyboardInterrupt:
        print("\n")
        print(Color.GREEN + "Thank You For Using")

ip_changer()