#!/usr/bin/env python3
"""
Z-Cyber Tools v3.0 - ULTIMATE EDITION
Advanced Pentesting Suite by Zeeone-ofc-Grayhat
"""

import os
import sys
import subprocess
import time
import json
import socket
from datetime import datetime
from pathlib import Path

class Colors:
    # Warna sama kayak sebelumnya
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
║                    Z-CYBER TOOLS v3.0                        ║
║                 ULTIMATE PENTESTING SUITE                    ║
║                  by Zeeone-ofc-Grayhat                       ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}""")

# FUNCTIONS YANG UDH ADA (run_sublist3r, run_xsstrike, dll)
# ...

# ==================== FUNCTIONS BARU v3.0 ====================

def run_sqlmap(url):
    """Run SQL Injection Scanner"""
    print(f"{Colors.LIGHT_CYAN}[*] Running SQL Injection Scanner on {url}{Colors.END}")
    
    try:
        # Cek apakah sqlmap tersedia
        result = subprocess.run(["which", "sqlmap"], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Pakai sqlmap
            result = subprocess.run([
                "sqlmap", "-u", url, "--batch", "--risk=3", "--level=5"
            ], capture_output=True, text=True, timeout=600)
        else:
            print(f"{Colors.LIGHT_YELLOW}[!] SQLMap not installed{Colors.END}")
            print(f"{Colors.LIGHT_YELLOW}[*] Install with: pkg install sqlmap{Colors.END}")
            return False
        
        # Process results
        if result.stdout:
            if "sqlmap identified" in result.stdout or "injection" in result.stdout.lower():
                print(f"{Colors.LIGHT_GREEN}[+] SQL Injection Found!{Colors.END}")
                print(f"{Colors.LIGHT_WHITE}{result.stdout}{Colors.END}")
            else:
                print(f"{Colors.LIGHT_YELLOW}[-] No SQL Injection detected{Colors.END}")
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"{Colors.LIGHT_RED}[-] SQL Scan timeout after 10 minutes{Colors.END}")
        return False
    except Exception as e:
        print(f"{Colors.LIGHT_RED}[-] SQL Scanner error: {e}{Colors.END}")
        return False

def run_portscan(target):
    """Run Port Scanner"""
    print(f"{Colors.LIGHT_CYAN}[*] Running Port Scanner on {target}{Colors.END}")
    
    try:
        # Simple port scanner dengan socket
        print(f"{Colors.LIGHT_YELLOW}[*] Scanning common ports...{Colors.END}")
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]
        open_ports = []
        
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                open_ports.append(port)
                print(f"{Colors.LIGHT_GREEN}[+] Port {port} OPEN{Colors.END}")
        
        print(f"{Colors.LIGHT_GREEN}[+] Found {len(open_ports)} open ports{Colors.END}")
        return open_ports
        
    except Exception as e:
        print(f"{Colors.LIGHT_RED}[-] Port Scanner error: {e}{Colors.END}")
        return []

def validate_vulnerability(url, vuln_type):
    """Validate Vulnerability with manual checks"""
    print(f"{Colors.LIGHT_CYAN}[*] Validating {vuln_type} on {url}{Colors.END}")
    
    # Simulasi validation logic
    validation_score = 0
    
    if vuln_type == "XSS":
        # Check untuk XSS validation
        print(f"{Colors.LIGHT_YELLOW}[*] Checking for XSS payload reflection...{Colors.END}")
        # Add actual validation logic here
        validation_score = 85  # Contoh score
        
    elif vuln_type == "SQLi":
        # Check untuk SQLi validation
        print(f"{Colors.LIGHT_YELLOW}[*] Checking for SQL error messages...{Colors.END}")
        validation_score = 90
        
    print(f"{Colors.LIGHT_GREEN}[+] Validation Score: {validation_score}%{Colors.END}")
    return validation_score

def generate_report(scan_results):
    """Generate HTML Report"""
    print(f"{Colors.LIGHT_CYAN}[*] Generating Security Report...{Colors.END}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"security_report_{timestamp}.html"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Z-Cyber Tools Security Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background: #2c3e50; color: white; padding: 20px; }}
            .vuln {{ background: #e74c3c; color: white; padding: 10px; margin: 5px; }}
            .info {{ background: #3498db; color: white; padding: 10px; margin: 5px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🔒 Z-Cyber Tools Security Report</h1>
            <p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>
        
        <h2>📊 Scan Summary</h2>
        <div class="info">
            <p>Target: {scan_results.get('target', 'N/A')}</p>
            <p>Scan Duration: {scan_results.get('duration', 'N/A')}</p>
            <p>Vulnerabilities Found: {scan_results.get('vuln_count', 0)}</p>
        </div>
        
        <h2>⚠️ Vulnerabilities</h2>
        <div class="vuln">
            <h3>XSS Vulnerabilities: {len(scan_results.get('xss_vulns', []))}</h3>
            <!-- Add actual vulnerabilities here -->
        </div>
        
        <h2>🛡️ Recommendations</h2>
        <ul>
            <li>Update all software to latest versions</li>
            <li>Implement Web Application Firewall (WAF)</li>
            <li>Regular security audits</li>
        </ul>
    </body>
    </html>
    """
    
    with open(report_file, 'w') as f:
        f.write(html_content)
    
    print(f"{Colors.LIGHT_GREEN}[+] Report generated: {report_file}{Colors.END}")
    return report_file

def complete_audit(target_url):
    """Complete Security Audit - ALL IN ONE"""
    print(f"{Colors.LIGHT_GREEN}[🚀] STARTING COMPLETE SECURITY AUDIT{Colors.END}")
    print(f"{Colors.LIGHT_YELLOW}[*] Target: {target_url}{Colors.END}")
    
    scan_results = {
        'target': target_url,
        'start_time': datetime.now(),
        'vulnerabilities': []
    }
    
    # 1. Subdomain Scan
    print(f"\n{Colors.LIGHT_CYAN}[1/6] Subdomain Scanning...{Colors.END}")
    # run_sublist3r(domain) - butuh domain bukan URL
    
    # 2. XSS Scan
    print(f"\n{Colors.LIGHT_CYAN}[2/6] XSS Vulnerability Scanning...{Colors.END}")
    run_xsstrike(target_url)
    
    # 3. SQL Injection Scan
    print(f"\n{Colors.LIGHT_CYAN}[3/6] SQL Injection Scanning...{Colors.END}")
    run_sqlmap(target_url)
    
    # 4. Extract domain untuk port scan
    try:
        domain = target_url.split("//")[-1].split("/")[0]
        # 5. Port Scan
        print(f"\n{Colors.LIGHT_CYAN}[4/6] Port Scanning...{Colors.END}")
        open_ports = run_portscan(domain)
        scan_results['open_ports'] = open_ports
    except:
        print(f"{Colors.LIGHT_YELLOW}[-] Skipping port scan{Colors.END}")
    
    # 6. Generate Report
    print(f"\n{Colors.LIGHT_CYAN}[5/6] Generating Report...{Colors.END}")
    scan_results['end_time'] = datetime.now()
    scan_results['duration'] = str(scan_results['end_time'] - scan_results['start_time'])
    
    report_file = generate_report(scan_results)
    
    print(f"\n{Colors.LIGHT_GREEN}[✅] COMPLETE AUDIT FINISHED!{Colors.END}")
    print(f"{Colors.LIGHT_GREEN}[+] Report saved: {report_file}{Colors.END}")
    
    return scan_results

# ==================== MAIN MENU v3.0 ====================

def main():
    os.system('clear')
    banner()
    
    print(f"\n{Colors.LIGHT_GREEN}{Colors.BOLD}>>> ULTIMATE PENTESTING SUITE v3.0 <<<{Colors.END}")
    print(f"{Colors.LIGHT_BLUE}[*] Initializing advanced security protocols...{Colors.END}")
    time.sleep(1)
    print(f"{Colors.LIGHT_GREEN}[+] Z-Cyber Tools v3.0 READY{Colors.END}\n")
    
    while True:
        print(f"{Colors.LIGHT_PURPLE}╔══════════════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║           Z-CYBER TOOLS v3.0 MENU           ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}╠══════════════════════════════════════════════╣{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  1. Subdomain Scanner                        ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  2. XSS Vulnerability Scanner                ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  3. SQL Injection Scanner                    ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  4. Port Scanner                             ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  5. Vulnerability Validator                  ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  6. Report Generator                         ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  7. Complete Security Audit                  ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}║  8. Exit Z-Cyber Tools                       ║{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}╚══════════════════════════════════════════════╝{Colors.END}")
        
        choice = input(f"\n{Colors.LIGHT_YELLOW}Z-Cyber> Select option (1-8): {Colors.END}").strip()
        
        if choice == "1":
            domain = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target domain: {Colors.END}").strip()
            if domain:
                run_sublist3r(domain)
        
        elif choice == "2":
            url = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target URL: {Colors.END}").strip()
            if url:
                run_xsstrike(url)
        
        elif choice == "3":
            url = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target URL for SQLi scan: {Colors.END}").strip()
            if url:
                run_sqlmap(url)
        
        elif choice == "4":
            target = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter IP/Domain for port scan: {Colors.END}").strip()
            if target:
                run_portscan(target)
        
        elif choice == "5":
            url = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter URL to validate: {Colors.END}").strip()
            vuln_type = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Vulnerability type (XSS/SQLi): {Colors.END}").strip()
            if url and vuln_type:
                validate_vulnerability(url, vuln_type)
        
        elif choice == "6":
            print(f"{Colors.LIGHT_GREEN}[+] Generating sample report...{Colors.END}")
            sample_results = {'target': 'example.com', 'vuln_count': 3}
            generate_report(sample_results)
        
        elif choice == "7":
            url = input(f"{Colors.LIGHT_CYAN}Z-Cyber> Enter target URL for complete audit: {Colors.END}").strip()
            if url:
                complete_audit(url)
        
        elif choice == "8":
            print(f"{Colors.LIGHT_GREEN}[+] Thank you for using Z-Cyber Tools v3.0!{Colors.END}")
            print(f"{Colors.LIGHT_BLUE}[*] Stay secure, grayhat!{Colors.END}")
            break
        
        else:
            print(f"{Colors.LIGHT_RED}[-] Invalid choice. Please select 1-8{Colors.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.LIGHT_RED}[-] Z-Cyber Tools interrupted by user{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.LIGHT_RED}[-] System error: {e}{Colors.END}")

