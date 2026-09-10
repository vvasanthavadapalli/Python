#program_15
s = input("Enter a sentence: ")
words = s.split()
print("Number of words:", len(words))

'''output:
Enter a sentence: practice like a devil and play like an angel
Number of words: 9 '''


#program_16
s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

'''output:
Enter a sentence: practice makes men perfect
Longest word: practice '''

#program_17
s = input("Enter a sentence: ")
words = s.split()
words.reverse()
print(" ".join(words))

'''output:
Enter a sentence: dont judge a book by its cover
cover its by book a judge dont '''

#program_18
s = input("Enter a sentence: ")
words = s.split()
result = []
for word in words:
    result.append(word[0].upper() + word[1:].lower())
print(" ".join(result))

'''sample output:
Enter a sentence: python is a programming language
Python Is A Programming Language '''

#program_19
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagrams")
else:
    print("Not anagrams")

'''output:
Enter first string: listen
Enter second string: silently
Not anagrams '''


