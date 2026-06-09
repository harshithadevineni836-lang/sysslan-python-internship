name = input("Enter name: ")

with open("records.txt", "a") as file:
    file.write(name + "\n")

print("\nSaved Records:")

with open("records.txt", "r") as file:
    print(file.read())