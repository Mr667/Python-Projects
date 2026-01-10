def km_to_Miles(km):
    return km*0.621371

def c_to_f(Celsius):
    return (Celsius * 9/5) + 32

print("1. Km to Miles | 2. Celsius to Fahrenheit")
choice = input("Select Conversion: ")
val = float(input("Enter the Value: "))

if choice == "1":
    print(f"{val} Km is {km_to_Miles(val):.2f} Miles")

elif choice == "2":
    print(f"{val}°C is {c_to_f(val):.2f}°F")