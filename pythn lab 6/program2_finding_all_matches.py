import re

text = "NASA and USA sent astronauts to SPACE for research."

# Find words written in capital letters
capital_words = re.findall(r"\b[A-Z]{2,}\b", text)
print("Capital words:", capital_words)

# Find words longer than 6 characters
print("Words longer than 6 characters:")

for x in re.finditer(r"\b[A-Za-z]{7,}\b", text):
    print(x.group(), "starts at", x.start())

# Find all dollar amounts
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r"\$\d+\.\d+", prices)
print("Dollar amounts:", amounts)

# Count the prices
print("Number of prices:", len(amounts))

'''output:
Capital words: ['NASA', 'USA', 'SPACE']
Words longer than 6 characters:
astronauts starts at 18
research starts at 42
Dollar amounts: ['$3.50', '$1.20', '$4.75']
Number of prices: 3  '''

