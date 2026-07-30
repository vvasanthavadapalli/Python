import sys

# Check if exactly two command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
else:
    # Convert arguments to integers
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Print their sum
    print("Sum =", num1 + num2)
    #output:Usage: python add.py <num1> <num2>