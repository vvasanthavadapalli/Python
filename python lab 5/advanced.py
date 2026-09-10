#program_20
str = input("Enter a string: ")
result = ""
for ch in str:
    if ch not in result:
        result += ch
print("Result:", result)

'''output:
Enter a string: string
Result: string '''


#program_21
s = input("Enter a string: ")
if s.isdigit():
    print("Contains only digits")
elif s.isalpha():
    print("Contains only alphabets")
elif s.isalnum():
    print("Contains alphabets and digits")
else:
    print("Contains special characters")

'''output:
Enter a string: age18
Contains alphabets and digits '''

#program_22
s = input("Enter a string: ")
for ch in s:
    if s.count(ch) > 1:
        print(ch, ":", s.count(ch))

'''output:
Enter a string: programming
r : 2
g : 2
r : 2
m : 2
m : 2
g : 2 '''

#program_23
s = input("Enter a string: ")
characters = list(s)
print("List:", characters)
result = "".join(characters)
print("String:", result)

'''output:
Enter a string: positive
List: ['p', 'o', 's', 'i', 't', 'i', 'v', 'e']
String: positive '''

#program_24
s = input("Enter an identifier: ")
if s.isidentifier():
    print("Valid identifier")
else:
    print("Invalid identifier")

'''output:
Enter an identifier: 18_age
Invalid identifier '''

#program_25
s = input("Enter a string: ")
sub = input("Enter substring: ")
index = -1
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        index = i
        break
print("Index:", index)

'''output:
Enter a string: hello world
Enter substring: world
Index: 6 '''




