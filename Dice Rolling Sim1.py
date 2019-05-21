from random import randint

question = input("Would you like to roll the dice of fate? ")

repeat = True
while repeat:
    print("You rolled ", randint(1, 6))
    print("You rolled ", randint(1, 6))
    print("Thanks for playing!")
    print("Do you want to roll again?")
    repeat = "yes" in input().lower()
    print("Thanks for playing")

