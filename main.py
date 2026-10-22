def calculate_avg(student_grades):
    total_grades = 0;
    count = 0
    for subject, grade in student_grades.items():
        total_grades += grade
        count += 1
    return total_grades / count

def find_highest(student_grades):
    max = 0
    sub = ""
    for subject, grade in student_grades.items():
        if grade > max:
            max = grade
            sub = subject
    print(f"Highest grade: {sub} : {max}")
def find_lowest(student_grades):
    min = 101
    sub = ""
    for subject, grade in student_grades.items():
        if grade < min:
            min = grade
            sub = subject
    print(f"Lowest grade: {sub} : {min}")

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
    find_lowest(student_grades)
    find_highest(student_grades)



