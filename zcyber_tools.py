#!/usr/bin/env python3
"""
Z-Cyber Tools v2.0
Advanced Pentesting Suite by Zeeone-ofc-Grayhat
"""

import os
import sys
import subprocess
import time
import requests
import pyfiglet
from pathlib import Path
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.style import Style
from rich.align import Align
from rich.console import Console

console = Console()

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
    text_banner = pyfiglet.figlet_format("ZCYBER",font="ansi_shadow").rstrip().splitlines()
    align_banner = "\n".join(line.center(54) for line in text_banner)
    border_banner = Panel(
        Text(align_banner, style="bold green"),
        border_style="bold blue", box=box.DOUBLE_EDGE,
        title="[bold yellow]ZCYBER_TOOLS[/bold yellow]",
        subtitle="[bold black][[bold white on purple]CODED BY ZEOONEOFC[/bold white on purple]][/bold black]",
        width=56
    )
    console.print(Align.center(border_banner))

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

def install_tools():
    """Install required tools"""
    print(f"{Colors.LIGHT_BLUE}[*] Installing Z-Cyber Tools...{Colors.END}")
    
    # Install system dependencies
    try:
        subprocess.run(["pkg", "install", "python", "git", "-y"], check=True)
        print(f"{Colors.LIGHT_GREEN}[+] System dependencies installed{Colors.END}")
    except subprocess.CalledProcessError:
        print(f"{Colors.LIGHT_RED}[-] Failed to install system dependencies{Colors.END}")
        return False
    
    # Install Python dependencies
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "requests", "dnspython", "lxml", "tldextract"], check=True)
        print(f"{Colors.LIGHT_GREEN}[+] Python dependencies installed{Colors.END}")
    except subprocess.CalledProcessError:
        print(f"{Colors.LIGHT_RED}[-] Failed to install Python dependencies{Colors.END}")
        return False
    
    # Clone Sublist3r
    if not os.path.exists("Sublist3r"):
        try:
            subprocess.run(["git", "clone", "https://github.com/aboul3la/Sublist3r.git"], check=True)
            # Install Sublist3r requirements
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "Sublist3r/requirements.txt"], check=True)
            print(f"{Colors.LIGHT_GREEN}[+] Sublist3r installed successfully{Colors.END}")
        except subprocess.CalledProcessError:
            print(f"{Colors.LIGHT_RED}[-] Failed to install Sublist3r{Colors.END}")
            return False
    
    # Clone XSStrike
    if not os.path.exists("XSStrike"):
        try:
            subprocess.run(["git", "clone", "https://github.com/s0md3v/XSStrike.git"], check=True)
            # Install XSStrike requirements
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "XSStrike/requirements.txt"], check=True)
            print(f"{Colors.LIGHT_GREEN}[+] XSStrike installed successfully{Colors.END}")
        except subprocess.CalledProcessError:
            print(f"{Colors.LIGHT_RED}[-] Failed to install XSStrike{Colors.END}")
            return False
    
    return True

def run_sublist3r(domain):
    """Run Sublist3r for subdomain enumeration"""
    print(f"{Colors.LIGHT_CYAN}[*] Running Subdomain Scanner on {domain}{Colors.END}")
    
    try:
        # Run Sublist3r
        result = subprocess.run([
            sys.executable, "Sublist3r/sublist3r.py",
            "-d", domain,
            "-o", f"subdomains_{domain}.txt"
        ], capture_output=True, text=True)
        
        # Print output in real-time
        if result.stdout:
            print(f"{Colors.LIGHT_WHITE}{result.stdout}{Colors.END}")
        
        if result.stderr:
            print(f"{Colors.LIGHT_RED}Errors: {result.stderr}{Colors.END}")
        
        # Check if output file was created
        output_file = f"subdomains_{domain}.txt"
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                subdomains = f.readlines()
            print(f"{Colors.LIGHT_GREEN}[+] Found {len(subdomains)} subdomains. Saved to {output_file}{Colors.END}")
            
            # Display first 10 subdomains
            print(f"{Colors.LIGHT_YELLOW}[*] First 10 subdomains:{Colors.END}")
            for i, subdomain in enumerate(subdomains[:10]):
                print(f"  {i+1}. {subdomain.strip()}")
            if len(subdomains) > 10:
                print(f"  ... and {len(subdomains) - 10} more")
        
        return True
        
    except Exception as e:
        print(f"{Colors.LIGHT_RED}[-] Error running Subdomain Scanner: {e}{Colors.END}")
        return False

def run_xsstrike(url):
    """Run XSStrike for XSS testing"""
    os.system(f"xsstrike -u '{url}' --crawl)

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
            domain = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target domain (e.g., example.com): {Colors.END}").strip()
            if domain:
                run_sublist3r(domain)
            else:
                print(f"{Colors.LIGHT_RED}[-] Please enter a valid domain{Colors.END}")
        
        elif choice == "2":
            url = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target URL (e.g., https://example.com/search.php): {Colors.END}").strip()
            if url:
                run_xsstrike(url)
            else:
                print(f"{Colors.LIGHT_RED}[-] Please enter a valid URL{Colors.END}")
        
        elif choice == "3":
            domain = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target domain for subdomain scan: {Colors.END}").strip()
            url = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target URL for XSS scan: {Colors.END}").strip()
            
            if domain and url:
                print(f"{Colors.LIGHT_YELLOW}[*] Starting complete security audit...{Colors.END}")
                run_sublist3r(domain)
                print(f"\n{Colors.LIGHT_BLUE}" + "═" * 60 + f"{Colors.END}")
                run_xsstrike(url)
                print(f"{Colors.LIGHT_GREEN}[+] Complete security audit finished!{Colors.END}")
            else:
                print(f"{Colors.LIGHT_RED}[-] Please enter both domain and URL{Colors.END}")
        
        elif choice == "4":
            print(f"{Colors.LIGHT_GREEN}[+] Thank you for using Z-Cyber Tools!{Colors.END}")
            print(f"{Colors.LIGHT_BLUE}[*] Stay secure, grayhat!{Colors.END}")
            break
        
        else:
            print(f"{Colors.LIGHT_RED}[-] Invalid choice. Please select 1-4{Colors.END}")
        
        print(f"\n{Colors.LIGHT_BLUE}" + "═" * 60 + f"{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.LIGHT_RED}[-] Z-Cyber Tools interrupted by user{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.LIGHT_RED}[-] System error: {e}{Colors.END}")
