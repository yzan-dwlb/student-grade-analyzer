
def calculate_avg(student_grades):
    total_grades = 0
    count = 0
    for subject, grade in student_grades.items():
        total_grades += grade
        count += 1
    if count == 0:
        return 0
    return total_grades / count


def find_highest(student_grades):
    maximum = -1
    sub = ""
    if len(student_grades) == 0:
        return None, None
    for subject, grade in student_grades.items():
        if grade > maximum:
            maximum = grade
            sub = subject
    return sub, maximum


def find_lowest(student_grades):
    minimum = 101
    sub = ""
    if len(student_grades) == 0:
        return None, None
    for subject, grade in student_grades.items():
        if grade < minimum:
            minimum = grade
            sub = subject
    return sub, minimum


print("Welcome to grade analyzer!")
while True:
    try:
        amount = int(input("Enter amount of courses: "))
        if amount <= 0:
            print("Please enter a positive number!")
        else:
            break
    except ValueError:
        print("Please enter a number!")

student_grades = {}
for i in range(amount):
    sub = input("Enter subject name: ")
    while True:
        try:
            grade = int(input("Enter subject grade: "))
            if grade > 100 or grade < 0:
                print("Please enter a grade between 0-100")
            else:
                student_grades[sub] = grade
                break

        except ValueError:
            print("Invalid input! Please enter a number.")
for subject, grade in student_grades.items():
    print(subject + ": " + f"{grade}")

print(f"The average grade is: {calculate_avg(student_grades)}")
sub1, minimum = find_lowest(student_grades)
sub2, maximum = find_highest(student_grades)
print(f"Highest Grade: {sub2} : {maximum}")
print(f"Lowest Grade: {sub1} : {minimum}")
print(student_grades)





