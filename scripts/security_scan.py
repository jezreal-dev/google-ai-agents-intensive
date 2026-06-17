import os
import sys
import re

# Regex pattern matching Google API Keys starting with AIzaSy
API_KEY_PATTERN = re.compile(r'AIzaSy[A-Za-z0-9_\-]{33}')

def scan_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            matches = API_KEY_PATTERN.findall(content)
            return matches
    except Exception as e:
        print(f"[-] Error reading {filepath}: {e}")
        return []

def main():
    print("[*] Starting automated credential leak scan...")
    flagged_files = {}
    
    # Walk through workspace files recursively
    for root, dirs, files in os.walk('.'):
        # Exclude git internals, configurations, and skills definitions
        if '.git' in root or '.github' in root or '.agents' in root:
            continue
            
        for file in files:
            filepath = os.path.join(root, file)
            # Skip python scripts themselves to avoid matching the regex definition!
            if file == 'security_scan.py':
                continue
                
            matches = scan_file(filepath)
            if matches:
                flagged_files[filepath] = len(matches)
                
    if flagged_files:
        print("\n[!] DANGER: Potential exposed credentials found:")
        for file, count in flagged_files.items():
            print(f"    - {file} ({count} match(es))")
        print("\n[!] Threat scan failed. Please remove the secrets before pushing.")
        return False
    else:
        print("\n[+] SUCCESS: No exposed API keys detected in workspace.")
        return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
