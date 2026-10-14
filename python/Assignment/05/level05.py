# Q37. Print Characters with Index

string=input("Enter a string: ")
for i in range(0,len(string)):
    print(i,string[i])

# Q38. Count Characters Without len()

string=input("Enter a string: ")
count=0
for i in string:
    count=count+1
print(count)

# Q39. Count Vowels and Consonants

string=input("Enter a string: ")
vowel_count=0
consonent_count=0
for i in string:
    if i.lower() in "aeiou" :
        vowel_count=vowel_count+1
    elif i.lower() not in " aeiou":
        consonent_count=consonent_count+1
print(f"Vowels = {vowel_count}, Consonents = {consonent_count}")

# Q40. Character Frequency

string=input("Enter a string: ")
frequency_count=input("Enter the string for the frequency count: ")
count=0
for i in string:
    if i==frequency_count:
        count=count+1

print(f"{frequency_count} = {count}")

# Q41. First Occurrence Position

string=input("Enter a string: ")
first_occurence=input("Enter the character for the first occurence: ")
found=False
for i in range(0,len(string)):
    if string[i]==first_occurence and not found:
        print(i)
        found=True
if not found:
    print("Not Found")


# Q42. Count Uppercase and Lowercase

s = input("Enter a string: ")
upper = 0
lower = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1

print("Uppercase =", upper, end=", ")
print("Lowercase =", lower)


# 43. Character Code Analyzer

string=input("Enter a string: ")
for i in range(0,len(string)):
    print(string[i],ord(string[i]))


# Q44. String Without Vowels

string=input("Enter a string: ")
no_vowel=""
for i in string:
    if i.lower() not in "aeiou":
        no_vowel=no_vowel+i
print(no_vowel)

