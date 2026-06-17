students = [
    "Harshita",
    "Riya",
    "Aman",
    "Rahul",
    "Priya"
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

with open("students.txt", "r") as file:
    data = file.readlines()

for name in data:
    print(name.strip())

print("Total Students:", len(data))

# output:
# Students List:
# Harshita
# Riya
# Aman
# Rahul
# Priya

# Total Students: 5