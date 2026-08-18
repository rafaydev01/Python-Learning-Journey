# ==========================================
# 1. LONG LISTS (Mutable Sequences)
# ==========================================

# A long list of dictionaries representing a user database
users_list = [
    {"id": 101, "name": "Alice", "role": "admin", "active": True, "balance": 1500.50},
    {"id": 102, "name": "Bob", "role": "editor", "active": False, "balance": 420.00},
    {"id": 103, "name": "Charlie", "role": "guest", "active": True, "balance": 0.00},
    {"id": 104, "name": "Diana", "role": "editor", "active": True, "balance": 890.75},
    {"id": 105, "name": "Ethan", "role": "guest", "active": False, "balance": 15.25},
    {"id": 106, "name": "Fiona", "role": "admin", "active": True, "balance": 2300.00},
    {"id": 107, "name": "George", "role": "guest", "active": True, "balance": 105.00},
]

# Modifying a list (Lists are mutable)
users_list.append({"id": 108, "name": "Hannah", "role": "editor", "active": True, "balance": 620.00})


# ==========================================
# 2. TUPLES (Immutable Sequences)
# ==========================================

# Tuples are excellent for fixed configuration data that shouldn't change
SYSTEM_ROLES = ("admin", "editor", "viewer", "guest")
MAX_LIMITS = (100, 500, 1000, 5000)

# A long list of tuples representing coordinate logs (lat, lon, timestamp)
location_logs = [
    (40.7128, -74.0060, "2026-08-18 10:00"),
    (34.0522, -118.2437, "2026-08-18 11:15"),
    (51.5074, -0.1278, "2026-08-18 12:30"),
    (35.6762, 139.6503, "2026-08-18 13:45"),
]


# ==========================================
# 3. COMPLEX CONDITIONS & LOOPS
# ==========================================

print("--- Processing User Database ---")

# Iterating through the long list and applying multiple conditions
for user in users_list:
    # Condition 1: Check if the role exists in our valid system roles tuple
    if user["role"] not in SYSTEM_ROLES:
        print(f"Alert: {user['name']} has an invalid role!")
        continue
        
    # Condition 2: Check account status and balance thresholds using logical operators
    if user["active"] and user["balance"] >= 1000:
        status_tier = "Premium Active User"
    elif user["active"] and 0 < user["balance"] < 1000:
        status_tier = "Standard Active User"
    elif not user["active"] and user["balance"] > 0:
        status_tier = "Suspended Account with Balance"
    else:
        status_tier = "Inactive / Zero Balance"

    # Condition 3: Nested condition for specific administrative privileges
    if user["role"] == "admin":
        if user["active"]:
            privilege = "Full Access Granted"
        else:
            privilege = "Access Revoked (Inactive)"
    else:
        privilege = "Standard Access Granted"

    # Output the processed data
    print(f"User: {user['name']} | Tier: {status_tier} | Permissions: {privilege}")


# ==========================================
# 4. ADVANCED LIST & TUPLE CONDITIONS
# ==========================================

print("\n--- Advanced Data Filtering ---")

# List comprehension with a conditional structure
# Creates a new list of names for active users with balances over $500
high_value_users = [user["name"] for user in users_list if user["active"] and user["balance"] > 500]
print("High Value Active Users:", high_value_users)

# Checking tuple structure inside a list using conditional slicing
if len(location_logs) >= 3:
    latest_log = location_logs[-1] # Get last item
    # Unpacking the tuple
    lat, lon, time = latest_log
    
    # Conditional check on numerical boundaries
    if lat > 0:
        hemisphere = "Northern"
    else:
        hemisphere = "Southern"
    print(f"Latest log is from the {hemisphere} hemisphere at {time}.")
