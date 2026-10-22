def calculate_avg(student_grades):
    total_grades = 0;
    count = 0
    for subject, grade in student_grades.items():
        total_grades += grade
        count += 1
    return total_grades / count

def find_highest(student_grades):
    maximum = 0
    sub = ""
    for subject, grade in student_grades.items():
        if grade > maximum:
            maximum = grade
            sub = subject
    return sub, maximum
def find_lowest(student_grades):
    minimum = 101
    sub = ""
    for subject, grade in student_grades.items():
        if grade < minimum:
            minimum = grade
            sub = subject
    return sub, minimum

print("Welcome to grade analyzer!")
student_grades = {
    "Mathematics": 92,
    "Statistics": 85,
    "Python": 96,
    "English": 88
}
for subject, grade in student_grades.items():
    print(subject + ": " + f"{grade}")

print(f"The average grade is: {calculate_avg(student_grades)}")
sub1, minimum = find_lowest(student_grades)
sub2, maximum = find_highest(student_grades)
print(f"Highest Grade: {sub2} : {maximum}")
print(f"Lowest Grade: {sub1} : {minimum}")
    



