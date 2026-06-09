while True:
    print("\n1. Addition")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))

        print("Result =", a + b)

    elif choice == "2":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")