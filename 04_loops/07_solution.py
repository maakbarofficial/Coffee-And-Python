while True:
    number = int(input("Enter value between 1 and 10:"))

    if 1 <= number <= 10:
        print("Valid number")
        break
    else:
        print("Invalid number")
