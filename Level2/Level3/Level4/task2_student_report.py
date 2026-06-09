name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\nStudent Report")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)