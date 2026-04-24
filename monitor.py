import os
import re
import time
from colorama import Style, Fore, init
from pyfiglet import figlet_format
import shutil
init(autoreset=True)

banner = figlet_format("SOC-SENTINEL", font = "slant")
print(Fore.CYAN + banner)

print("="*50)
print(Fore.RED + "  🚨 Real-Time Threat Detection Tool")
print("="*50)
print(Fore.BLUE + "     👨‍💻 Developer  : Script-Jockey")
print(Fore.BLUE + "     🛡️  Module     : Brute Force Detection")
print(Fore.BLUE + "     📦 Version   :  1.0.1")
print("="*50)


log_file = "/var/log/auth.log"
failed_attempts = {}
alerted_ips = set()

print(Fore.BLUE + "\n[+] Montitoring Started......\n")

def extract_ip(line):
    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
    if match:
        return match.group(0)
    return "Unknown"

try:
    with open(log_file, "r") as f:
        f.seek(0,2)

        while True:
            line = f.readline()

            if not line:
                time.sleep(0.5)
                continue

            if "Failed password" in line:
                ip = extract_ip(line)
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

                print(Fore.MAGENTA + f"⚠ Failed login from {ip} | Attempts: {failed_attempts[ip]}")

                if failed_attempts[ip] >= 5:
                    if ip not in alerted_ips:
                        print(Fore.RED + "🔥 [ALERT] : Brute Force Attack Detected")
                        print(Fore.GREEN + f"Attacker IP : {ip}")
                        alerted_ips.add(ip)

except KeyboardInterrupt:
    print(Fore.YELLOW + "\n[!] Monitoring Stopped by User")