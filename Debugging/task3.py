# Debugging Challenge - Part 3: Data Conversion Errors
# These programs have bugs with data types and conversions
# Fix the bugs so the programs calculate correctly
# DO NOT delete code - fix it!


def program_1():
    # This program should calculate total cost of movie tickets
    # Example: 4 tickets at $12 each = $48 total
    print("Welcome to the Movie Theater!")
    tickets = input("How many tickets? ")
    price_each = 12
    total = tickets * price_each
    print(f"Number of tickets: {tickets}")
    print(f"Price per ticket: ${price_each}")
    print(f"Total cost: ${total}")


def program_2():
    # This program should calculate the sum of two numbers
    # Example: 25 + 17 = 42
    print("Addition Calculator")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")


def program_3():
    # This program should convert temperature from Celsius to Fahrenheit
    # Formula: F = C * 9/5 + 32
    # Example: 25 Celsius = 77.0 Fahrenheit
    print("Temperature Converter")
    celsius = input("Enter temperature in Celsius: ")
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")


def program_4():
    # This program should calculate pay based on hours and rate
    # Example: 40 hours at $15.50/hour = $620.00
    print("Paycheck Calculator")
    hours = input("Hours worked: ")
    rate = input("Hourly rate: ")
    pay = hours * rate
    print(f"Hours: {hours}")
    print(f"Rate: ${rate}/hour")
    print(f"Total pay: ${pay}")


def program_5():
    # This program should calculate the area of a rectangle
    # Example: 8.5 width x 4 height = 34.0 area
    print("Rectangle Area Calculator")
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    area = width * height
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Area: {area}")


def program_6():
    # This program should calculate a restaurant bill with tip
    # Example: $45.50 bill with 20% tip = $54.60 total
    print("Tip Calculator")
    bill = input("Enter bill amount: ")
    tip_percent = input("Enter tip percentage: ")
    tip_amount = float(bill) * tip_percent / 100
    total = float(bill) + tip_amount
    print(f"Bill: ${bill}")
    print(f"Tip ({tip_percent}%): ${tip_amount}")
    print(f"Total: ${total}")
