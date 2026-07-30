# Take multiple values in one line separated by spaces
numbers = input("Enter numbers separated by spaces: ")

# Split the input and convert each value to an integer
numbers = list(map(int, numbers.split()))

# Print the sum
print("Sum =", sum(numbers))
#output:Enter numbers separated by spaces: 5 6 3
#Sum = 14