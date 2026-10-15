import math
# Q53. Second Largest Digit
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
largest = -1
second_largest = -1

for i in range(digit_count):
    digit = num % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit
    num = num // 10
print(second_largest)

# Q54. Longest Consecutive Equal Character Run
s = input("Enter a string: ")
max_run = 0
current_run = 0
prev_char = ""

for char in s:
    if char == prev_char:
        current_run += 1
    else:
        current_run = 1
        prev_char = char
    if current_run > max_run:
        max_run = current_run
print(max_run)

# Q55. Most Frequent Character — Controlled Approach
s = input("Enter a string: ")
target = input("Enter a target character: ")
count = 0
total_chars = 0

for char in s:
    total_chars += 1
    if char == target:
        count += 1

frequency = (count / total_chars) * 100
print(f"Count = {count}, Frequency = {frequency}%")

# Q56. Running Digit Sum Until the End
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
running_sum = 0

for i in range(digit_count):
    running_sum += num % 10
    print(running_sum)
    num = num // 10

# Q57. Number with Most Even Digits
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
even_count = 0
odd_count = 0

for i in range(digit_count):
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10

if even_count > odd_count:
    print("More Even Digits")
elif odd_count > even_count:
    print("More Odd Digits")
else:
    print("Equal")

# Q58. Alternating Digit Sum
num = int(input("Enter a Number: "))
digit_count = int(math.log10(num)) + 1
alt_sum = 0
sign = 1

for i in range(digit_count):
    digit = num % 10
    alt_sum += digit * sign
    sign *= -1  # Flips between 1 and -1
    num = num // 10
print(alt_sum)

# Q59. Output Prediction — Accumulator Trap
"""
Expected Output:
2
6
12
20
30
"""

# Q60. Output Prediction — Condition Inside Loop
"""
Expected Output:
5
Explanation: The loop runs from 1 to 10. The condition `i % 2 == 0` checks if the number is even. There are 5 even numbers between 1 and 10 (2, 4, 6, 8, 10).
"""

# Q61. Debug the Accumulator
"""
1. Identify the mistake: `sum = i` overwrites the accumulator instead of adding to it.
2. Correct the program:
sum = 0
for i in range(1, 6):
    sum = sum + i
print(sum)

3. Explanation: The accumulator `sum` needs to retain its previous value and add the new value of `i` to it in every iteration.
"""
