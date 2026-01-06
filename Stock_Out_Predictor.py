# Inventory: [Item name, Current Stocks, Units sold Last 30 days]
Warehouse = [
    ["iphone 15", 100, 1200],
    ["MacBook M3", 150, 20],
    ["Airpods", 250, 100],
    ["Apple Watch", 50, 12]
]

print(f"{'Item':<15}| {'Daily Burn':<12}| {'Days Remaining'}")
print("-" * 45)

for item, Stock, Monthly_sales in Warehouse:
    Daily_burn_rates = Monthly_sales / 30
    Days_until_Empty = Stock / Daily_burn_rates

# Alert Logic
    alert = "⚠️  REORDER NOW" if Days_until_Empty < 7 else "✅ Stable"

    print(f"{item:<15} | {Daily_burn_rates:>10.2f} | {int(Days_until_Empty):>2} Days ({alert})")