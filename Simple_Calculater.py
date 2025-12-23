Num1 = float(input("Enter you Number: "))
Op = input("Enter you Operator (+,-,*,/): ")
Num2 = float(input("Enter your Number: "))


#float() vs int(): We use float() because users might want to calculate decimals (like 5.5), not just whole numbers.

if Op == '+':
    print(Num1 + Num2)
elif Op == '-':
    print(Num1-Num2)
elif Op == '*':
    print(Num1*Num2)
elif Op =='/':
    print(Num1/Num2)
else:
    print("Invalid Operator")
    