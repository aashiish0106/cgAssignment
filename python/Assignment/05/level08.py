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

