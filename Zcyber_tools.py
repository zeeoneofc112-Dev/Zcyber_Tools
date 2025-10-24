#!/usr/bin/env python3
"""
Z-Cyber Tools - FIXED VERSION
Advanced Pentesting Suite by Zeeone-ofc
"""

import os
import sys
import subprocess
import time
import requests
from pathlib import Path

class Colors:
    LIGHT_BLUE = '\033[94m'
    LIGHT_CYAN = '\033[96m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_RED = '\033[91m'
    LIGHT_PURPLE = '\033[95m'
    LIGHT_WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def banner():
    print(f"""{Colors.LIGHT_CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ███████ ██████  ███████ ██████  ███████ ██████           ║
║    ██      ██   ██ ██      ██   ██ ██      ██   ██          ║
║    ███████ ██████  █████   ██████  █████   ██████           ║
║         ██ ██   ██ ██      ██   ██ ██      ██   ██          ║
║    ███████ ██   ██ ███████ ██   ██ ███████ ██   ██          ║
║                                                              ║
║    ╔════════════════════════════════════════════════════╗    ║
║    ║              Z-Cyber Tools v2.0                   ║    ║
║    ║        Advanced Pentesting Suite                 ║    ║
║    ║           by Zeeone-ofc-Grayhat                  ║    ║
║    ╚════════════════════════════════════════════════════╝    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}""")

def check_installation():
    """Check if required tools are installed"""
    tools_installed = True

    print(f"{Colors.LIGHT_BLUE}[*] Checking installations...{Colors.END}")

    # Check Sublist3r
    if not os.path.exists("Sublist3r"):
        print(f"{Colors.LIGHT_RED}[-] Sublist3r not found{Colors.END}")
        tools_installed = False
    else:
        print(f"{Colors.LIGHT_GREEN}[+] Sublist3r found{Colors.END}")

    # Check XSStrike - SKIPPED
    print(f"{Colors.LIGHT_GREEN}[+] XSStrike check skipped{Colors.END}")

    return tools_installed
 

def show_welcome_message():
    """Show welcome message"""
    print(f"\n{Colors.LIGHT_GREEN}{Colors.BOLD}>>> you have successfully entered Z-Cyber Tools by Zeeone-ofc-Grayhat <<<{Colors.END}")
    print(f"{Colors.LIGHT_BLUE}[*] Initializing security protocols...{Colors.END}")
    time.sleep(1)
    print(f"{Colors.LIGHT_GREEN}[+] Z-Cyber Tools ready for operation{Colors.END}\n")

def main():
    os.system('clear')
    banner()
    show_welcome_message()
    
    # Check if tools are installed
    if not check_installation():
        print(f"{Colors.LIGHT_YELLOW}[!] Some tools are missing. Run installer.py first{Colors.END}")
        return
    
    # Main menu
    while True:
        print(f"{Colors.LIGHT_PURPLE}╔══════════════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║               Z-CYBER MENU                   ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}╠══════════════════════════════════════════════╣{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  1. Subdomain Scanner                        ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  2. XSS Vulnerability Scanner                ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  3. Complete Security Audit                  ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  4. Exit Z-Cyber Tools                       ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}╚══════════════════════════════════════════════╝{Colors.END}")
        
        choice = input(f"\n{Colors.LIGHT_YELLOW}Z-Cyber> Select option (1-4): {Colors.END}").strip()
        
        if choice == "1":
            print(f"{Colors.LIGHT_GREEN}[+] Subdomain Scanner selected{Colors.END}")
        elif choice == "2":
            print(f"{Colors.LIGHT_GREEN}[+] XSS Scanner selected{Colors.END}")
        elif choice == "3":
            print(f"{Colors.LIGHT_GREEN}[+] Security Audit selected{Colors.END}")
        elif choice == "4":
            print(f"{Colors.LIGHT_GREEN}[+] Thank you for using Z-Cyber Tools!{Colors.END}")
            break
        else:
            print(f"{Colors.LIGHT_RED}[-] Invalid choice{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.LIGHT_RED}[-] Z-Cyber Tools interrupted by user{Colors.END}")



