import math

# Q62. Daily Expense Analyzer
n = int(input("Enter number of days: "))
total = 0
highest = 0
lowest = float('inf')

for i in range(n):
    exp = int(input(f"Enter expense for day {i+1}: "))
    total += exp
    if exp > highest:
        highest = exp
    if exp < lowest:
        lowest = exp

print(f"Total: {total}\nHighest: {highest}\nLowest: {lowest}")

# Q63. Student Marks Analyzer
n = int(input("Enter number of subjects: "))
total = 0
highest = 0
lowest = float('inf')

for i in range(n):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

average = total / n
print(f"Total: {total}\nAverage: {average}\nHighest: {highest}\nLowest: {lowest}")

# Q64. Attendance Analyzer
n = int(input("Enter number of working days: "))
present = 0
absent = 0

for i in range(n):
    status = input("Enter status (P/A): ").upper()
    if status == 'P':
        present += 1
    elif status == 'A':
        absent += 1

attendance = (present / n) * 100
print(f"Present: {present}\nAbsent: {absent}\nAttendance: {attendance:.2f}%")

# Q65. Electricity Usage Analyzer
n = int(input("Enter number of days: "))
total_units = 0
days_above_10 = 0

for i in range(n):
    units = int(input(f"Enter units for day {i+1}: "))
    total_units += units
    if units > 10:
        days_above_10 += 1

print(f"Total Units: {total_units}\nDays Above 10: {days_above_10}")

# Q66. Shopping Bill Analyzer
n = int(input("Enter number of products: "))
total_bill = 0
above_1000 = 0

for i in range(n):
    price = int(input(f"Enter price for product {i+1}: "))
    total_bill += price
    if price > 1000:
        above_1000 += 1

print(f"Total Bill: {total_bill}\nProducts Above 1000: {above_1000}")

# Q67. Login Attempt Analyzer
n = int(input("Enter number of login attempts: "))
success = 0
failed = 0

for i in range(n):
    attempt = input("Enter attempt (success/failed): ").lower()
    if attempt == "success":
        success += 1
    elif attempt == "failed":
        failed += 1

success_rate = (success / n) * 100
print(f"Successful: {success}\nFailed: {failed}\nSuccess Rate: {success_rate}%")

# Q68. Number Profile
num = int(input("Enter a positive integer: "))
digit_count = int(math.log10(num)) + 1
total_sum = 0
largest = -1
smallest = 10
even_count = 0
odd_count = 0

for i in range(digit_count):
    digit = num % 10
    total_sum += digit
    
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
        
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    num = num // 10

print(f"Digits: {digit_count}\nSum: {total_sum}\nLargest: {largest}\nSmallest: {smallest}\nEven Digits: {even_count}\nOdd Digits: {odd_count}")

# Q69. String Balance Challenge
s = input("Enter a string: ")
total_chars = 0
vowels = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index_chars = 0

for i in range(len(s)):
    total_chars += 1
    char = s[i]
    
    if i % 2 == 0:
        even_index_chars += 1
        
    if char != " ":
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
            
        if char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1

print(f"Total Characters: {total_chars}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Even Index Characters: {even_index_chars}")


