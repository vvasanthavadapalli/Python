
#integers
age = 18
current_year = 2026
birth_year = current_year - age
print("Type of age:", type(age))
print("Type of current_year:", type(current_year))
print("Type of birth_year:", type(birth_year))
print("Age in 2050:", 2050 - birth_year)
#task
x = 17
y = 5
print("Integer Division:", x // y)
print("Modulus:", x % y)
print("Exponent:", x ** 2)

#strings
first = "Vasantha"
last = "Vadapalli"

full_name = first + " " + last

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title Case:", full_name.title())
print("Length:", len(full_name))
#task
print("First Character:", full_name[0])
print("Last Character:", full_name[-1])

print("First Name:", full_name[:full_name.index(" ")])

#boolean(bool)
is_raining = True
has_umbrella = False

print("Type of is_raining:", type(is_raining))
print("Type of has_umbrella:", type(has_umbrella))

print("is_raining and has_umbrella:", is_raining and has_umbrella)
print("is_raining or has_umbrella:", is_raining or has_umbrella)
print("not is_raining:", not is_raining)

print("True + True =", True + True)
print("False * 5 =", False * 5)

#output
'''Type of age: <class 'int'>
Type of current_year: <class 'int'>
Type of birth_year: <class 'int'>
Age in 2050: 42
Integer Division: 3
Modulus: 2
Exponent: 289
Uppercase: VASANTHA VADAPALLI
Lowercase: vasantha vadapalli
Title Case: Vasantha Vadapalli
Length: 18
First Character: V
Last Character: i
First Name: Vasantha
Type of is_raining: <class 'bool'>
Type of has_umbrella: <class 'bool'>
is_raining and has_umbrella: False
is_raining or has_umbrella: True
not is_raining: False
True + True = 2
False * 5 = 0'''
