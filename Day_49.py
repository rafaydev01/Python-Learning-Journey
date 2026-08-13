def process_inventory():
    # 1. Setup inventory data (List of dictionaries)
    inventory = [
        {"name": "Laptop", "price": 1200, "stock": 4, "category": "Electronics"},
        {"name": "Phone", "price": 800, "stock": 15, "category": "Electronics"},
        {"name": "Desk Chair", "price": 150, "stock": 0, "category": "Furniture"},
        {"name": "Coffee Maker", "price": 90, "stock": 8, "category": "Kitchen"},
        {"name": "Backpack", "price": 45, "stock": 25, "category": "Accessories"},
    ]

    # 2. Initialize tracking lists
    restock_alerts = []
    premium_items = []
    affordable_items = []

    print("--- Processing Inventory Status ---")

    # 3. Loop through the list and apply multiple conditions
    for item in inventory:
        name = item["name"]
        price = item["price"]
        stock = item["stock"]

        # Check stock levels (Nested condition)
        if stock == 0:
            print(f"❌ ALERT: {name} is completely OUT OF STOCK!")
            restock_alerts.append(name)
        elif stock < 5:
            print(f"⚠️ WARNING: {name} is running low ({stock} left).")
            restock_alerts.append(name)
        else:
            print(f"✅ AVAILABLE: {name} has healthy stock ({stock} units).")

        # Categorize items by price range
        if price >= 500:
            premium_items.append(name)
        elif 100 <= price < 500:
            # Item is mid-range, we skip adding to lists for this example
            pass
        else:
            affordable_items.append(name)

    # 4. Display final summary reports
    print("\n" + "="*30)
    print("📋 FINAL INVENTORY REPORT")
    print("="*30)
    
    print(f"Items needing restock: {restock_alerts}")
    print(f"Luxury/Premium items (>= $500): {premium_items}")
    print(f"Budget-friendly items (< $100): {affordable_items}")

# Run the program
if __name__ == "__main__":
    process_inventory()












