# main.py

import os
import time

def banner():
    os.system('clear')
    print('''
\033[1;92m
███████╗██╗  ██╗ ██████╗ ██╗  ██╗ █████╗  ██████╗ ██╗  ██╗
██╔════╝██║  ██║██╔═══██╗██║  ██║██╔══██╗██╔════╝ ██║  ██║
███████╗███████║██║   ██║███████║███████║██║  ███╗███████║
╚════██║██╔══██║██║   ██║██╔══██║██╔══██║██║   ██║██╔══██║
███████║██║  ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
\033[0m
             Created By: Shohagh 🐥 With Jerry AI 💻
''')
    time.sleep(1)

def main_menu():
    banner()
    print('''
\033[1;96m
[1] Information Gathering
[2] Email2IP Tracker
[3] Brute Force Modules
[4] Reverse Shell Generator
[5] APK Payload Generator (Coming Soon)
[6] Launch Auto VPN Checker
[7] Update Tool
[0] Exit
\033[0m
''')

    choice = input("➤ Enter option: ")

    if choice == "1":
        os.system("python modules/info_gather.py")
    elif choice == "2":
        os.system("python modules/email2ip.py")
    elif choice == "3":
        os.system("python modules/bruteforce.py")
    elif choice == "4":
        os.system("python modules/reverseshell.py")
    elif choice == "5":
        print("⚠️ APKGen Module coming soon...")
    elif choice == "6":
        os.system("python utils/vpncheck.py")
    elif choice == "7":
        os.system("git pull")
    elif choice == "0":
        print("👋 Exiting... Bye Shohagh dada!")
        exit()
    else:
        print("❌ Invalid option!")
        time.sleep(1)
        main_menu()

if __name__ == "__main__":
    main_menu()
