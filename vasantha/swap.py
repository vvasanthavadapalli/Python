# (a) Swapping using a temporary third variable

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping using a temporary variable:")
print("a =", a)
print("b =", b)


# (b) Swapping using Python's tuple unpacking

a = 10
b = 20

print("\nBefore swapping again:")
print("a =", a)
print("b =", b)

# Swap using tuple unpacking
a, b = b, a

print("\nAfter swapping using tuple unpacking:")
print("a =", a)
print("b =", b)
#output:Before swapping:
#a = 10
#b = 20

#After swapping using a temporary variable:
#a = 20
#b = 10

#Before swapping again:
#a = 10
#b = 20

#After swapping using tuple unpacking:
#a = 20
#b = 10