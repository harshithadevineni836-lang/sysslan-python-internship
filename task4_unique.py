# Check whether all numbers are unique

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numbers = []

for row in grid:
    numbers.extend(row)

if len(numbers) == len(set(numbers)):
    print("All numbers in the grid are unique.")
else:
    print("Duplicate numbers found in the grid.")