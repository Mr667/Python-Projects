password = input("Create a password: ")
has_digit = False
has_upper = False

if len(password) >= 8:
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Strong Password! ✅")
else:
    print("Weak Password. Must be 8+ chars, have a number and an uppercase letter. ❌")