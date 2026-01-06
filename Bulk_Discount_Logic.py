unit_price = 50
Quantity = int(input("Enter the Quantity: "))

if Quantity >= 100:
    Discount = 0.20  # 20% off
elif Quantity >= 50:
    Discount = 0.10  # 10% off
elif Quantity >= 25:
    Discount = 0.05  # 5% off
else:
    Discount = 0

total_cost = (unit_price*Quantity) * (1 - Discount)
Savings = (unit_price*Quantity)*Discount

print(f"Discount Applied: {Discount*100}%")
print(f"Final Invoice Amount: ${total_cost:,.2f}")
print(f"You Saved: ${Savings:,.2f} Today")