import re

# 1. Hide email addresses
text = "Contact abc@gmail.com or xyz@yahoo.com"

result = re.sub(r"\w+@\w+\.\w+", "[EMAIL HIDDEN]", text)
print("Hidden emails:", result)


# 2. Change Doe, John into John Doe
name = "Doe, John"

result = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", name)
print("Changed name:", result)


# 3. Double every number
sentence = "I have 3 apples and 5 oranges."

def double_number(x):
    return str(int(x.group()) * 2)

result = re.sub(r"\d+", double_number, sentence)
print("Doubled numbers:", result)


# 4. Remove repeated punctuation
sample = "Wait!!! What??? Really!!!"

result, count = re.subn(r"([!?])\1+", r"\1", sample)

print("After removing repeated punctuation:", result)
print("Number of replacements:", count)

'''output:
Hidden emails: Contact [EMAIL HIDDEN] or [EMAIL HIDDEN]
Changed name: John Doe
Doubled numbers: I have 6 apples and 10 oranges.
After removing repeated punctuation: Wait! What? Really!
Number of replacements: 3  '''
