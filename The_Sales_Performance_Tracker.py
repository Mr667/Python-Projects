# a lsit representing  sales transactions for the days
sales_data = [150.50, 3200.00, 450.25, 120.00, 5000.00, 890.00, 25.50]

#1. Define business thresholds
high_value_limits = 1000

#2. Initial counters and lists
total_revenue = sum(sales_data)
high_value_sales = []
total_tax = 0.10
total_tax_amount = total_revenue * 0.10


#3. Processing the data
for sales in sales_data:
    total_revenue += sales # Cumulative sum

    if sales >= high_value_limits:
        high_value_sales.append(sales)

#4. Calculate key performance indicators (KPI)
avg_transaction_value = total_revenue / len(sales_data)
count_high_value = len(high_value_sales)

print("---- DAILY SALES SUMMARY ----")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Avg. Ticket size: ${avg_transaction_value:,.2f}")
print(f"High-Value Trades: {count_high_value}")
print(f"Large Transaction: {high_value_sales}")
print(f"Net Profit: {total_tax_amount:,.2f}")