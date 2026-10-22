print("Welcome to grade analyzer!")
student_grades = {
  "Mathematics" : 92,
  "Statistics" : 85,
  "Python" : 96,
  "English" : 88
}
for subject, grade in student_grades.items():
  print(subject + ": " + f"{grade}")
