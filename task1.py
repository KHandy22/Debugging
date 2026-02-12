# Debugging Challenge - Part 1: Code Errors
# Fix the bugs in each snippet - just run to test!
# DO NOT delete code - fix it!


def snippet_1():
    # This program should display a personalized greeting
    # Expected output: Hello, Alex! You are 15 years old.
    name = "Alex"
    age = 15
    print(f"Hello, {Name}!")
    print(f"You are {age} years old.")


def snippet_2():
    # This program should calculate and display pizza party info
    # Expected output should show 24 total slices and 3 slices per person
    pizzas = 3
    slices_per_pizza = 8
    people = 8
    total_slices = pizzas * slices_per_pizza
    slices_each = total_slices / people
    print(f"Total slices: {total_slices}")
    print(f"Slices per person: {slices_each)


def snippet_3():
    # This program should check if a student passed and print their grade
    # Student scored 75, which is passing (60 or above)
    student_name = "Jordan"
    score = 75
    passing_score = 60
    if score >= passing_score
        result = "passed"
    else:
        result = "did not pass"
    print(f"{student_name} scored {score} points.")
    print(f"{student_name} {result} the test.")


def snippet_4():
    # This program should compare two game scores and announce the winner
    # Player 1 scored 150, Player 2 scored 150, so it should be a tie
    player1_score = 150
    player2_score = 150
    print(f"Player 1: {player1_score} points")
    print(f"Player 2: {player2_score} points")
    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    elif player1_score = player2_score:
        print("It's a tie!")


def snippet_5():
    # This program should display a weather report
    # Expected: Show temperature and a message based on conditions
    temperature = 72
    is_sunny = True
    print(f"Current temperature: {temperture} degrees")
    if is_sunny:
        print("It's a sunny day!")
    else:
        print("It's cloudy today.")


def snippet_6():
    # This program should calculate the cost of buying books
    # 3 books at $12.99 each = $38.97 total
    book_title = "Python Basics"
    price = 12.99
    quantity = 3
    total = price * quantity
    print(f"Book: {book_title}")
    print(f"Price each: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total: $ total")
