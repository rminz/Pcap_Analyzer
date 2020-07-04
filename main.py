import sys
import IP_Extractor
from constant import Colors

AUTHOR = "ARMIN ZIAIE TABARI"
VERSION = "v1.0"


if __name__ == '__main__':
    print("______                  ___              _                    ".center(40))
    print("| ___ \                / _ \            | |                   ".center(40))
    print("| |_/ /__ __ _ _ __   / /_\ \_ __   __ _| |_   _ _______ _ __ ".center(40))
    print("|  __/ __/ _` | '_ \  |  _  | '_ \ / _` | | | | |_  / _ \ '__|".center(40))
    print("| | | (_| (_| | |_) | | | | | | | | (_| | | |_| |/ /  __/ | ".center(40))
    print("\_|  \___\__,_| .__/  \_| |_/_| |_|\__,_|_|\__, /___\___|_|  ".center(40))
    print("              | |                           __/ |             ".center(40))
    print("              |_|                          |___/              ".center(40))
    print(" ")
    print((" "+AUTHOR+ " - "+VERSION+"\n").center(60))
    
    print("1) Extract IP addresses and check with AbuseIPDB")
    print("2) Exit")

    try:
        choice = int(input('[*] Enter your choice: '))
        if choice == 1:
            FileName = input('[-] Enter your file name: ')
            if FileName == "":
                print(Colors.REDBG+"[Error]: "+Colors.END+"Provide an input file for process")
                sys.exit(1)
            else:
                IP_Extractor.extract_IP(FileName)
                sys.exit(1)
        elif choice == 2:
            print("[*] Exiting... ")
            sys.exit(1)
        else:
            print("[*] Invalid choice")
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)








  
 


