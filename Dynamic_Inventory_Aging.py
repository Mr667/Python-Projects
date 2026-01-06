from datetime import datetime

# Inventory: [Item, Unit_Cost, Date_Added (YYYY-MM-DD)]
inventory = [
    ("Laptop X", 1200, "2023-05-10"),
    ("Monitor Y", 300, "2025-11-20"),
    ("Cable Z", 25, "2025-08-01"),
]

today = datetime(2026, 1, 3) # Using our current year 2026
dead_stock_threshold = 90 # Days

print("--- Inventory Aging Report ---")
for item, cost, date_str in inventory:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    days_in_stock = (today - date_obj).days
    
    status = "DEAD STOCK" if days_in_stock > dead_stock_threshold else "HEALTHY"
    
    print(f"{item:10} | {days_in_stock:3} Days | Status: {status}")