def add_student(name,marks):
    return{
        "name":name,
        "marks":marks
    }

def cal_average(marks):
    return sum(marks) /len(marks)

def check_result(avg):
    if avg >= 40:
        return "Passed"
    else:
        return "Failed"
    
student = add_student(
    "Harshita",
    [70, 80, 60]
)

average = cal_average(student["marks"])

result = check_result(average)

print("Student:", student["name"])
print("Average:", average)
print("Result:", result)

# output:
# Student: Harshita
# Average: 70.0
# Result: Passed