# (a) Multi-line statement using the line continuation character (\)

total1 = 10 + 20 + 30 + \
         40 + 50 + 60

print("Total using \\ :", total1)


# (b) Equivalent multi-line statement using implicit continuation with parentheses ()

total2 = (
    10 + 20 + 30 +
    40 + 50 + 60
)

print("Total using ():", total2)
#output:Total using \ : 210
#Total using (): 210