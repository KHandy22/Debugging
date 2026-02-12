# Debugging Challenge - Part 2: Input Syntax Errors
# These programs have bugs in their input statements
# Fix the bugs so the programs run correctly
# DO NOT delete code - fix it!


def program_1():
    # This program should greet the user and ask about their day
    name = input("What is your name? )
    feeling = input("How are you feeling today? ")
    print(f"Hello, {name}!")
    print(f"Glad to hear you are feeling {feeling}.")


def program_2():
    # This program should ask for the user's favorite things
    # and display them back
    color = imput("What is your favorite color? ")
    food = input("What is your favorite food? ")
    print(f"Your favorite color is {color}.")
    print(f"Your favorite food is {food}.")


def program_3():
    # This program should ask for two test scores
    # and tell the user which one was higher
    print("Enter your two test scores:")
    score1 = int(input("Score 1: "))
    score2 = int(input("Score 2: "):
    if score1 > score2:
        print(f"Your first score ({score1}) was higher!")
    elif score2 > score1:
        print(f"Your second score ({score2}) was higher!")
    else:
        print(f"Both scores are the same: {score1}!")


def program_4():
    # This program should calculate the user's birth year
    # based on their current age
    name = input("What is your name? ")
    age = int(input["How old are you? "])
    current_year = 2026
    birth_year = current_year - age
    print(f"Hello, {name}!")
    print(f"You were born in {birth_year}.")
