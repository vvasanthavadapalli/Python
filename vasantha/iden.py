
def display_message():
    print("Function called successfully!")



class Student:
    def __init__(self, name):
        self.name = name

age = 20


MAX_VALUE = 100


student_id = 101


s = Student("Sai")


print("Variable (age):", age)
print("Constant-style name (MAX_VALUE):", MAX_VALUE)
print("Name with underscore (student_id):", student_id)
print("Class object name:", s.name)

# Call the function
display_message()
#output: Variable (age): 20
# Constant-style name (MAX_VALUE): 100
# Name with underscore (student_id): 101
# Class object name: Sai