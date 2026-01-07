# Write a program which will keep adding a stream of number inputted by the user. The adding stops as soon as the user press the Q.

sum = 0
while(True):
    User_Input = input("Enter the item price or Press q to exit: \n")
    if(User_Input != "q"):
        sum = sum + int(User_Input)
        print(f"Order total so far {sum}")
    else:
        print(f"Your Bill total is {sum}. Thanks for visiting")
        break
