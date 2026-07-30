# Trying to use keywords as variable names

for = 5
True = 10


# Error messages:
#   File "example.py", line 3
#     for = 5
#         ^
# SyntaxError: invalid syntax
#
# If you comment out the first line and run again:
#
#   File "example.py", line 4
#     True = 10
#     ^^^^
# SyntaxError: cannot assign to True