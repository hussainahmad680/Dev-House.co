###   print(age)
#value()



try:
  age = int(input("Enter your age:"))
  income = 200000
  risk = income / age 
  print(age)
except ZeroDivisionError:
  print("Age cannot be zero:")
except ValueError:
  print("Invalid Value")