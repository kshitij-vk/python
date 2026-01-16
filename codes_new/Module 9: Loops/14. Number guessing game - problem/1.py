import random

print("Welcome to the Number guessing game! \nThe Secret number is between 1 to 50")


counter = 10
random_num = random.randint(1,50)

while counter != 0:
    guessed_number = int(input("Enter your guess: "))
    if guessed_number != random_num:
        counter = counter - 1
        if guessed_number > random_num:
            print('Wrong guess! Try lower number')
        else:
            print('Wrong guess! Try higher number')
        print(f'You have {counter} attempts left')

    else:
        print(f'You won! The number is {random_num}')
        break

if counter == 0:
    print("You lost the game noob!!")