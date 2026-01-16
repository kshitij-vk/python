import random

print("Welcome to the game of rolling a Dice!")

while True:
    choice = input("Press 'Enter' to roll the dice or 'q' to quit.")
    choice = choice.strip()
    if choice == 'q':
        print("Thankyou for playing!")
        break
    elif choice == '':
        number = random.randint(1,6)
        print(f"Number is {number}")
    else:
        print("Invalid input!")
        
print("Game Over!!!")