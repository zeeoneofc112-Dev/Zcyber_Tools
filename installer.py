#!/usr/bin/env python3
"""
Zcyber_Tools Installer
by Kenzo - Grayhat
"""

import os
import time

def banner():
    print("\033[94m")
    print("╔══════════════════════════════════╗")
    print("║         Zcyber_Tools             ║")
    print("║           INSTALLER              ║")
    print("║         by Kenzo - Grayhat       ║")
    print("╚══════════════════════════════════╝")
    print("\033[0m")

def main():
    banner()
    print("[+] Installing dependencies...")
    time.sleep(1)
    
    # Update package
    os.system("pkg update -y && pkg upgrade -y")
    
    # Install python & git
    os.system("pkg install python git -y")
    
    # Install python packages
    os.system("pip install requests beautifulsoup4")
    
    print("\n[+] Installation complete!")
    print("[+] Run: python Zcyber_tools.py")

if __name__ == "__main__":
    main()
