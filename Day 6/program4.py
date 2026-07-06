class student:

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)

student1 = student("Hussain", 123)
student1.display()