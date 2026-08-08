student1 = {"name": "Vasantha", "roll": 23}
student2 = student1
student3 = {"name": "Maya", "roll": 32}
print(student1 == student2)
print(student1 is student2)
print(student1 == student3)
print(student1 is student3)

'''output:
True
True
False
False
'''
