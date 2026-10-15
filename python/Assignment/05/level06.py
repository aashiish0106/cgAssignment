# Level 6 — Midpoint, Half & String Logic

# Q45. Find the Middle Character

# s = input()
# mid = len(s) // 2

# for i in range(len(s)):
#     if i == mid:
#         print(s[i])

# Q46. First Half and Second Half

string=input("Enter a string with even no. of character: ")

half=len(string)/2

first_half=""
second_half=""

for i in range(len(string)):
    if i<half:
        first_half=first_half+string[i]
    else:
        second_half=second_half+string[i]
print("First half: ",first_half)
print("Second half: ",second_half)

import math

# Q47. Split a String by Length — Odd vs Even
s = input("Enter a string: ")
n = len(s)
half = n // 2
first_half = ""
second_half = ""
mid = ""

for i in range(n):
    if i < half:
        first_half += s[i]
    elif n % 2 != 0 and i == half:
        mid = s[i]
    else:
        second_half += s[i]

print("First Half:", first_half)
if mid != "":
    print("Middle:", mid)
print("Second Half:", second_half)

# Q48. Compare Two Halves
s = input("Enter a string of even length: ")
n = len(s)
half = n // 2
first_half = ""
second_half = ""

for i in range(n):
    if i < half:
        first_half += s[i]
    else:
        second_half += s[i]

if first_half == second_half:
    print("Equal Halves")
else:
    print("Different Halves")

# Q49. Mirror the String
s = input("Enter a string: ")
n = len(s)
is_symmetric = True

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_symmetric = False

if is_symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")

# Q50. Alternate Character Extraction
s = input("Enter a string: ")
alt_string = ""

for i in range(len(s)):
    if i % 2 == 0:
        alt_string += s[i]
print(alt_string)

# Q51. Count Characters at Even and Odd Indexes
s = input("Enter a string: ")
even_count = 0
odd_count = 0

for i in range(len(s)):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even Index = {even_count}, Odd Index = {odd_count}")

# Q52. Swap Adjacent Characters
s = input("Enter a string with even length: ")
swapped = ""

for i in range(0, len(s), 2):
    swapped += s[i+1] + s[i]
print(swapped)

