import csv
grades = {
    "physics": 95,
    "calculus": 88,
    "programming": 100
}


def load_grades(file_name = "grades"):
    student_grades = {}
    with open(f"{file_name}.csv", "r", newline="") as file:
        reader =csv.reader(file)
        for row in reader:
            if(row[1] != "Grade"):
                student_grades[row[0]] = int(row[1])

    return student_grades


def save_grades(student_grades, file_name = "grades"):
    with open(f"{file_name}.csv", "w", newline="") as file:
        writer =csv.writer(file)
        writer.writerow(["Subject", "Grade"])
        for subject, grade in student_grades.items():
            writer.writerow([subject, grade])

    
if __name__ == "__main__":  
    save_grades(grades)
    print(load_grades())