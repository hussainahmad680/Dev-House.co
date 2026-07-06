first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
roll_number = int(input("Enter Roll Number: "))
department = input("Enter Department Name: ")
subject_1marks = int(input("Enter Subject 1 Marks: "))
subject_2marks = int(input("Enter Subject 2 Marks: "))
subject_3marks = int(input("Enter Subject 3 Marks: "))
first_name = first_name.strip()
last_name = last_name.strip()
department = department.strip().upper()
full_name = (first_name + " " + last_name).title()
def calculate_result(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    percentage = total / 3
    return total, percentage
total_marks, percentage = calculate_result(
    subject_1marks,
    subject_2marks,
    subject_3marks
)
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "Fail"
if percentage >= 50:
    status = "Promoted"
else:
    status = "Not Promoted"
def student_report(name, roll_no, department, total, percentage, grade, status):
    print("\nRESULT ")
    print("Student Name :", name)
    print("Roll Number  :", roll_no)
    print("Department   :", department)
    print("Total Marks  :", total)
    print("Percentage   :", f"{percentage:.2f}%")
    print("Grade        :", grade)
    print("Status       :", status)
    
student_report(
    full_name,
    roll_number,
    department,
    total_marks,
    percentage,
    grade,
    status
)
print()
student_report(
    grade=grade,
    status=status,
    percentage=percentage,
    total=total_marks,
    department=department,
    name=full_name,
    roll_no=roll_number
)
subjects = ["Computer Science", "Mathematics", "English"]
print("\nSubjects:")
for subject in subjects:
    print(subject)
student = {
    "Name": full_name,
    "Roll Number": roll_number,
    "Department": department,
    "Grade": grade
}
print("\nStudent Dictionary:")
for key, value in student.items():
    print(key, ":", value)