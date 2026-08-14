import math

# ==========================================
# 1. CORE DATA STRUCTURE INITIALIZATION
# ==========================================

# Raw sensor data: (Timestamp, Sensor_ID, Reading_Value, Status_Code)
raw_signals = [
    (1710000000, "TEMP_01", 23.5, "OK"),
    (1710000060, "PRESS_01", 101.3, "OK"),
    (1710000120, "TEMP_01", 42.1, "WARN"),
    (1710000180, "VOLT_02", 12.0, "OK"),
    (1710000240, "TEMP_01", 98.6, "CRIT"),
    (1710000300, "PRESS_01", 105.7, "WARN"),
    (1710000360, "VOLT_02", 11.2, "WARN"),
    (1710000420, "TEMP_02", 21.0, "OK"),
    (1710000480, "PRESS_01", 145.2, "CRIT"),
    (1710000540, "VOLT_02", 8.5, "CRIT"),
]

# Threshold configurations: (Warning_Limit, Critical_Limit)
temp_limits = (40.0, 85.0)
press_limits = (105.0, 140.0)
volt_limits = (11.0, 13.0)  # For voltage, values outside this range are issues

# Master lists for routing categorized logs
operational_backlog = []
critical_incident_archive = []
investigation_queue = []

# ==========================================
# 2. PROCESSING AND CONDITIONAL ROUTING
# ==========================================

print("=== STARTING AUTOMATED DATA AUDIT ===")

for record in raw_signals:
    # Unpacking the tuple elements
    timestamp, device_id, value, reported_status = record
    
    # Flag to track if the data point matches its reported state
    is_validated = True
    calculated_status = "OK"

    # Multi-layered conditional branching based on string matching
    if device_id.startswith("TEMP"):
        # Nested conditional logic using tuple boundary metrics
        if value >= temp_limits[1]:
            calculated_status = "CRIT"
        elif value >= temp_limits[0]:
            calculated_status = "WARN"
        else:
            calculated_status = "OK"

    elif device_id.startswith("PRESS"):
        if value >= press_limits[1]:
            calculated_status = "CRIT"
        elif value >= press_limits[0]:
            calculated_status = "WARN"
        else:
            calculated_status = "OK"

    elif device_id.startswith("VOLT"):
        # Double-bounded conditional checks
        if value < volt_limits[0] or value > volt_limits[1]:
            # Sub-routing depending on severity of divergence
            variance = abs(12.0 - value)
            if variance > 2.0:
                calculated_status = "CRIT"
            else:
                calculated_status = "WARN"
        else:
            calculated_status = "OK"
    else:
        # Fallback condition for unknown hardware profiles
        print(f"Unknown hardware footprint detected: {device_id}")
        investigation_queue.append((timestamp, device_id, "UNKNOWN_HARDWARE"))
        continue

    # Identity and conformity evaluations
    if calculated_status != reported_status:
        is_validated = False
        discrepancy_tag = f"MISMATCH: Logged({reported_status}) vs Calculated({calculated_status})"
        investigation_queue.append((timestamp, device_id, discrepancy_tag))

    # Building enriched payload tuples
    processed_payload = (timestamp, device_id, value, calculated_status, is_validated)

    # Master routing logic using compound list evaluation conditions
    if calculated_status == "CRIT" or not is_validated:
        critical_incident_archive.append(processed_payload)
    elif calculated_status == "WARN":
        operational_backlog.append(processed_payload)
    else:
        # Simple list append for clean telemetry
        operational_backlog.insert(0, processed_payload) # Prepend clean entries for processing sequence

print(f"Audit Complete. Records Processed: {len(raw_signals)}")

# ==========================================
# 3. ADVANCED LIST MANIPULATION & COMPREHENSIONS
# ==========================================

print("\n=== SYSTEM HEALTH METRICS ===")

# List comprehension filtering out anomalies from operational_backlog
valid_clean_readings = [item[2] for item in operational_backlog if item[3] == "OK" and item[4] is True]

# Inline conditional handling for math operations on lists
average_healthy_value = sum(valid_clean_readings) / len(valid_clean_readings) if valid_clean_readings else 0.0
print(f"Mean performance metrics for verified stable nodes: {average_healthy_value:.2f}")

# Extracting a distinct sorted list of critical device tags via list slicing and operations
critical_devices = [entry[1] for entry in critical_incident_archive]
# Emulating a unique list via filtering loops
unique_critical_devices = []
for dev in critical_devices:
    if dev not in unique_critical_devices:
        unique_critical_devices.append(dev)
        
print(f"Devices flagged for immediate physical inspection: {unique_critical_devices}")

# ==========================================
# 4. TUPLE immutability VERIFICATION & REPORTING
# ==========================================

print("\n=== GENERATING COMPLIANCE REPORT ===")

# Creating a high-security summary tuple that cannot be modified by downstream processes
summary_report = (
    len(raw_signals),
    len(critical_incident_archive),
    len(operational_backlog),
    len(investigation_queue)
)

print(f"Total Telemetry Evaluated : {summary_report[0]}")
print(f"Critical System Faults    : {summary_report[1]}")
print(f"Standard Operational Logs : {summary_report[2]}")
print(f"Integrity Mismatch Flags  : {summary_report[3]}")

# Showcase of structural slice checks on lists
if len(critical_incident_archive) > 0:
    print("\n--- Top Critical Incidents Preview ---")
    # Grabbing the last two critical items using list slicing
    for critical_item in critical_incident_archive[-2:]:
        print(f"Device: {critical_item[1]} | Metric: {critical_item[2]} | Validated: {critical_item[4]}")

# Final system safety determination based on list state evaluation
if len(critical_incident_archive) >= 3 or summary_report[3] > 1:
    sys_status_tuple = ("RED_ALERT", "System requires manual administrative override.")
elif len(operational_backlog) > len(raw_signals) / 2:
    sys_status_tuple = ("YELLOW_AMBER", "System operational but showing severe wear trends.")
else:
    sys_status_tuple = ("GREEN_NOMINAL", "System healthy.")

print(f"\nFINAL SYSTEM STATUS: [{sys_status_tuple[0]}] -> {sys_status_tuple[1]}")
