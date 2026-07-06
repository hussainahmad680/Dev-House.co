#def get_students():
  ###  roll_number = input("Enter your Roll Number:")
   # return name, roll_number
#name, roll_number = get_students()
#print(name)
#print(roll_number)






####  department = input("Enter your department name:")
    ###name, roll_number, department, marks = gets_student()
#print(name)
#print(roll_number)
#print(department)
#print(marks)


#def gets_student():
 #  print(========STUDENT REPORT=========)
  #  name = input ("Enter your Full name:")
   # roll_number = input ("Enter your Roll Number:")
    #marks = input ("Enter your full marks")
 #   return name, roll_number, marks
#name, roll_number, marks = gets_student()
#print(name)
#print(roll_number)
#print(marks)




def gets_student(): 
    name = input ("Enter your name:")
    roll_number = input ("Enter your roll number:")
    english_marks = int(input ("Enter your marks in English subject:"))
    computer_marks = int(input ("Enter your marks in Computer subject:"))
    math_marks = int(input ("Enter your marks in Math subject:"))
    return name, roll_number, english_marks, computer_marks, math_marks
name, roll_number,english_marks, math_marks, computer_marks = gets_student()
print(name)
print(roll_number)
print(english_marks)
print(computer_marks)
print(math_marks)
def total_marks(english_marks,computer_marks,math_marks):
    total = english_marks+computer_marks+math_marks
    return total
name, roll_number, english_marks, math_marks, computer_marks = gets_student()
print("Total Marks:", total)