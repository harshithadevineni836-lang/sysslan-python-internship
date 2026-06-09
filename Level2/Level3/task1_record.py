records = []

while True:
    name = input("Enter name: ")
    age = input("Enter age: ")

    records.append({"Name": name, "Age": age})

    choice = input("Add another record? (y/n): ")
    if choice.lower() != 'y':
        break

print("\nRecords:")
for record in records:
    print(record)