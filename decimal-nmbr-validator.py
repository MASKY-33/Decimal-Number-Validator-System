# Learning "try...except" using a (while-loop)


while True:
    number = input("Give a number: ").lower()

    if number == "stop":
        print("Bye!")
        break

    try:
        digit = float(number)
        print("Decimal-number successfully processed")
    except ValueError:
        print("Invalid input, try again.")
