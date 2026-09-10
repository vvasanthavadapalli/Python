#program_6
str=input('enter a string:')
ch=input('enter a character to count:')
count=0
for i in str:
    if i==ch:
        count+=1
print('occurances:',count)

'''sample output:
enter a string:failure is a stepping stone to success
enter a character to count:s
occurances: 6 '''

#program_7
str=input('enter a string:')
result=' '
for ch in str:
    if ch!=' ':
        result+=ch
print('string without spaces:',result)

'''sample output:
enter a string:all the greatest acheivers faced a failure atleast once.
string without spaces:  allthegreatestacheiversfacedafailureatleastonce. '''

#program_8
str=input('enter string:')
old=input('enter old character/word:')
new=input('enter new character/word:')
print('result:', str.replace(old,new))

'''sample output:
enter string:success needs patience
enter old character/word:patience
enter new character/word:consistency
result: success needs consistency '''

#program_9
str1=input('enter first string:')
str2=input('enter secoend string:')
result=' '.join([str1,str2])
print('result:', result)

'''sample output:
enter first string:success needs
enter secoend string:patience
result: success needs patience '''

#program_10
str=input('enter a string:')
print('result:', str.swapcase())

'''sample output:
enter a string:steps
result: STEPS '''

