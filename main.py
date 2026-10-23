def get_student_grades():
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
        while True:
            sub = input("Enter subject name: ").strip().lower()
            if not sub:
                print("Course name can not be empty!")
                continue
            if sub in student_grades:
                print("Duplicate course name, please enter a new course!")
            else:
                break
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

    return student_grades


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

if __name__ == "__main.py__":
    print("Welcome to grade analyzer!")
    student_grades = get_student_grades()
    for subject, grade in student_grades.items():
        print(f"{subject}: {grade}")

    print(f"The average grade is: {calculate_avg(student_grades)}")
    sub1, minimum = find_lowest(student_grades)
    sub2, maximum = find_highest(student_grades)
    print(f"Highest Grade: {sub2} : {maximum}")
    print(f"Lowest Grade: {sub1} : {minimum}")
    print(student_grades)

