#program_1
str=input('enter a string:')
print('length of a string', len(str))

'''sample output:
enter a string:programming is a skill
length of a string 22 '''

#program_2
str=input('enter a string:')
#without using slicing
rev=' '
for ch in str:
    rev=ch+rev
print('reverse:',rev)
#using slicing
print('Reverse:', str[::-1])

'''sample output:
enter a string:python
reverse: nohtyp 
Reverse: nohtyp '''

#program_3
check=input('enter string:')
if check==check[::-1]:
    print(check, 'is a palindrome')
else:
    print(check, 'is not a polindrome')

'''sample output:
enter string:amma
amma is a palindrome '''

#program_4
str=input('enter a string:')
print('uppercase of a string:', str.upper())
print('lowercase of a string:', str.lower())

'''sample output:
enter a string:Language
uppercase of a string: LANGUAGE
lowercase of a string: language '''

#program_5
str=input('enter string:')
vowels=0
consonants=0
digits=0
spaces=0
for ch in str:
    if ch.lower() in 'aeiou':
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch==' ':
        spaces+=1
print('vowels:', vowels)
print('consonants:', consonants)
print('digits:',digits)
print('spaces:',spaces)

'''sample output:
enter string:Never give up
vowels: 5
consonants: 6
digits: 0
spaces: 2 '''
    

