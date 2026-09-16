import re


# 5.1 Email Validator

def is_valid_email(email):
    pattern = r"^[\w.]+@[\w.-]+\.[A-Za-z]{2,6}$"
    return bool(re.fullmatch(pattern, email))


emails = [
    "abc@gmail.com",
    "student@yahoo.in",
    "hello@test.org",
    "user123@mail.com",
    "a@b.c",
    "no-at-sign.com",
    "user@gmail",
    "user@.com"
]

print("Email Validation:")

for email in emails:
    print(email, ":", is_valid_email(email))


# 5.2 Phone Number Extractor

text = """
Call 555-123-4567 or (555) 123-4567.
Another number is 555.222.3333.
"""

pattern = r"\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}"

numbers = re.findall(pattern, text)

print("\nPhone Numbers:")

for number in numbers:

    # Remove brackets and symbols
    digits = re.sub(r"\D", "", number)

    # Convert into standard format
    normal = re.sub(
        r"(\d{3})(\d{3})(\d{4})",
        r"\1-\2-\3",
        digits
    )

    print(number, "->", normal)


# 5.3 Date Extraction and Reformatting

text = "Dates are 15/08/2026 and 20/09/2026."

pattern = r"(\d{2})/(\d{2})/(\d{4})"

dates = re.findall(pattern, text)

print("\nDates found:", dates)

result = re.sub(pattern, r"\3-\2-\1", text)

print("Dates in ISO format:", result)


# 5.4 HTML and Whitespace Cleanup

def clean_text(html):

    # Remove HTML tags
    html = re.sub(r"<.*?>", "", html)

    # Replace multiple spaces, tabs and new lines
    html = re.sub(r"\s+", " ", html)

    return html.strip()


html = """
<p>Hello   <b>World</b></p>
<p>Welcome    to Python.</p>
"""

result = clean_text(html)

print("\nClean text:", result)


# 5.5 Password Strength Checker

def check_password(password):

    failed = []

    if len(password) < 8:
        failed.append("8 characters")

    if not re.search(r"[A-Z]", password):
        failed.append("uppercase letter")

    if not re.search(r"[a-z]", password):
        failed.append("lowercase letter")

    if not re.search(r"\d", password):
        failed.append("digit")

    if not re.search(r"[!@#$%^&*]", password):
        failed.append("special symbol")

    return failed


passwords = [
    "Hello@123",
    "hello123",
    "HELLO123",
    "HelloWorld"
]

print("\nPassword Checking:")

for password in passwords:

    result = check_password(password)

    if len(result) == 0:
        print(password, "-> Strong password")
    else:
        print(password, "-> Failed:", result)

'''output:
Email Validation:
abc@gmail.com : True
student@yahoo.in : True
hello@test.org : True
user123@mail.com : True
a@b.c : False
no-at-sign.com : False
user@gmail : False
user@.com : False

Phone Numbers:
555-123-4567 -> 555-123-4567
(555) 123-4567 -> 555-123-4567
555.222.3333 -> 555-222-3333

Dates found: [('15', '08', '2026'), ('20', '09', '2026')]
Dates in ISO format: Dates are 2026-08-15 and 2026-09-20.

Clean text: Hello World Welcome to Python.

Password Checking:
Hello@123 -> Strong password
hello123 -> Failed: ['uppercase letter', 'special symbol']
HELLO123 -> Failed: ['lowercase letter', 'special symbol']
HelloWorld -> Failed: ['digit', 'special symbol']  '''
        
