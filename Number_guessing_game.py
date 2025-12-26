import random
target = random.randint(1, 10)
guess = None

#print(f"You choose {guess}. Computer choose {target}")

Attempt = 0
while guess != target:
    guess = int(input("Enter the Number Between 1 to 10: "))
    Attempt += 1

    if guess < target:
        print("Too Low!")
    elif guess > target:
        print("Too High!")

print("Correct! You WIN.")
print(f"Efficiency Metric: {Attempt} Attemps.")
