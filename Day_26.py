# =====================================================================
# CYBERSECURITY TRAINING LAB: AUTOMATED SCRIPT SCANNER (LAB 03)
# ALIGNED WITH: SHRADHA DIDI (APNA COLLEGE) PYTHON COURSE - LECTURE 1 & 2
# CONCEPTS: DATA FILTERING, STRING ANALYSIS, AND CONDITIONAL ALERTS
# =====================================================================

print("=====================================================================")
print("         ADVANCED ATTACK DETECTION SYSTEM - MONITORING ACTIVE        ")
print("=====================================================================")

print("\n--- PHASE 1: RECONNAISSANCE & TARGET ACQUISITION ---")

# Step 1: Assigning environmental variables (Lecture 1)
target_ip = "192.168.1.105"
active_scanners_count = 4
is_proxy_enabled = True

# Step 2: Testing connection and string formatting
print(f"[!] Target IP Under Observation: {target_ip}")
print(f"[!] Active Network Scanners Running: {active_scanners_count}")
print(f"[!] Proxy Redirection Secured: {is_proxy_enabled}")


print("\n--- PHASE 2: PACKET INSPECTION & STRING SLICING (LECTURE 2) ---")

# Extracting clean payload text from encrypted-looking logs
raw_network_packet = "SECURITY_THREAT_DETECTED_BY_MALWARE_SCANNER"

print(f"Total Packet Length: {len(raw_network_packet)} bytes")
# Slicing the first part of the string to catch the alert status
print(f"Alert Status Code: {raw_network_packet[0:15]}")

# Replacing text for clean reporting
clean_report = raw_network_packet.replace("_", " ")
print(f"Clean Human Readable Report: {clean_report}")


print("\n--- PHASE 3: AUTOMATED FIREWALL RESPONSE (CONDITIONS) ---")

# Real-world dynamic security classification logic from Lecture 2
threat_score = int(input("Enter detected threat severity score (1 to 10): "))

if threat_score >= 8:
    print("[-] CRITICAL: Severe threat! Isolating target host instantly.")
    print("[-] ACTION: Email alert dispatched to Lead Cyber Security Officer.")
elif threat_score >= 5:
    print("[!] MODERATE: Suspicious behaviour. Activating deep packet logging.")
else:
    print("[+] LOW: Safe traffic profile. No action needed.")


print("\n=====================================================================")
print("MISSION CHECKPOINT: Keep grinding, secure the future, unlock the BMW!")
print("=====================================================================")
