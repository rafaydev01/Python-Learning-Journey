is_logged_in = True
has_permission = True

if is_logged_in:
    print("Welcome! You are logged in.")  # Branch 1 (Level 1)
    
    if has_permission:
        print("Access Granted to Dashboard.")  # Inside Branch 1 (Level 2)
    else:
        print("No permission to view this.")  # Inside Branch 1 (Level 2)
        
else:
    print("Please login first.")  # Branch 2 (Level 1)
