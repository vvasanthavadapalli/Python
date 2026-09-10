#program_11
str=input('enter a string:')
print('first character:', str[0])
print('last character:', str[-1])

'''sample output:
enter a string:python
first character: p
last character: n '''

#program_12
str=input('enter string:')
print('every secoend elements in the string:',str[1::2])

'''sample output:
enter string:success
every secoend elements in the string: ucs '''

#program_13
string=input('enter string:')
sub_string=input('enter string:')
start_index=string.find(sub_string)
length=len(sub_string)
if start_index!=-1 and string[start_index:start_index + length] == sub_string:
    print('sub_string belongs to strinng.')
else:
    print('sub_string not belongs to string.')

'''output:
enter string:every programming language follows certain syntax
enter string:python
sub_string not belongs to string. '''

#program_14
s = input("Enter a string: ")
ch = input("Enter character: ")
first = -1
last = -1
for i in range(len(s)):
    if s[i] == ch:
        if first == -1:
            first = i
        last = i
print("First occurrence:", first)
print("Last occurrence:", last)

'''output:
Enter a string: circumstances
Enter character: c
First occurrence: 0
Last occurrence: 10 '''



