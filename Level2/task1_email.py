# Email Address Validator

email = input("Enter your email address: ")

if "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rindex(".")

    if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
        print("Valid Email Address")
    else:
        print("Invalid Email Address")
else:
    print("Invalid Email Address")