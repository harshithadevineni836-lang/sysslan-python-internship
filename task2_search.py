# Check whether a number exists in the grid

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

number = int(input("Enter a number to search: "))

found = False

for row in grid:
    if number in row:
        found = True
        break

if found:
    print(f"{number} exists in the grid.")
else:
    print(f"{number} does not exist in the grid.")