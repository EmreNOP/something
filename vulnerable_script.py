# vulnerable_script.py
import os
import sys
# app.py
import requests

print("Testing Dependabot...")

def ping_host(hostname):
    """
    Pings a host. This function is VULNERABLE to command injection
    because it builds a command string with untrusted input.
    """
    print(f"--- Pinging {hostname} ---")
    
    # VULNERABLE LINE:
    # User input is directly concatenated into a shell command.
    # An attacker can "inject" other commands using ";" or "&&".
    command = f"ping -c 3 {hostname}"
    os.system(command)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vulnerable_script.py <hostname>")
        print("Example (malicious): python vulnerable_script.py '8.8.8.8; ls -la'")
        sys.exit(1)
        
    user_input = sys.argv[1]
    ping_host(user_input)
