import re


# 1. Python variable name

pattern = r"[A-Za-z_][A-Za-z0-9_]*"

names = ["_count2", "2fast", "total_sum"]

print("Variable names:")

for name in names:
    if re.fullmatch(pattern, name):
        print(name, "is valid")
    else:
        print(name, "is invalid")


# 2. Find cat, dog or bird

sentence = "I have a cat and a dog. My friend has a bird."

pattern = r"\b(cat|dog|bird)\b"

result = re.findall(pattern, sentence)

print("\nPets found:", result)


# 3. Find hexadecimal color codes

colors = "The colors are #FFAA00, #000 and #12ABCD."

pattern = r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"

result = re.findall(pattern, colors)

print("Hexadecimal colors:", result)


# 4. Parse a log line using named groups

line = "2024-06-01 08:15:32 ERROR Disk full"

pattern = (
    r"(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>\w+) "
    r"(?P<message>.*)"
)

result = re.fullmatch(pattern, line)

print("\nLog details:")
print("Date:", result.group("date"))
print("Time:", result.group("time"))
print("Level:", result.group("level"))
print("Message:", result.group("message"))

'''output:
Variable names:
_count2 is valid
2fast is invalid
total_sum is valid

Pets found: ['cat', 'dog', 'bird']
Hexadecimal colors: ['#FFAA00', '#000', '#12ABCD']

Log details: 
Date: 2024-06-01
Time: 08:15:32
Level: ERROR
Message: Disk full  '''
