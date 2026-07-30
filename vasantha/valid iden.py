import keyword

identifiers = ["2value", "value_2", "_hidden", "class", "my-var", "MyClass", "total$"]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(f"{name} -> Valid Identifier")
    else:
        print(f"{name} -> Invalid Identifier")
        #output:2value -> Invalid Identifier
#value_2 -> Valid Identifier
#_hidden -> Valid Identifier
#class -> Invalid Identifier
#my-var -> Invalid Identifier
#MyClass -> Valid Identifier
#total$ -> Invalid Identifier
