#Topic 1: Type Casting

# int()
# float()
# str()
# bool()

# Question 1 — String to Integer

age = "25"
convert_age=int(age)
print(convert_age)
print(type(convert_age))

# Question 2 — String to Float

marks = "75.5"
convert_marks=float(marks)
print(convert_marks)
print(type(convert_marks))

# Question 3 — Integer to Float

number = 50
convert_number=float(number)
print(convert_number)
print(type(convert_number))

# Question 4 — Float to Integer

marks = 85.9
convert_marks=int(marks)
print(convert_marks)
print(type(convert_marks))

# Question 5 — Integer to String

roll_number = 101
convert_number=str(roll_number)
print(convert_number)
print(type(convert_number))

# Question 6 — Multiple Conversions

print(type(int("18")))
print(type(float("92.5")))
print(type(str(100)))
print(type(int(45.8)))

# Question 7 — Predict the Output

a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))

#output
# 20
# 10
# 25
# <class 'int'>
# <class 'int'>
# <class 'str'>

# Question 8 — Debug Type Casting

# age = "19"
# new_age = age + 1

# print("Age:", new_age)

age = "19"
new_age = int(age) + 1

print("Age:", new_age)

# Question 9 — Marks Conversion

marks = "85"
print(int(marks)+5)

# Question 10 — Price Conversion

price = "1499.50"
print(float(price)+99.50)

# Topic 2: Arithmetic Operators

# Operator	Meaning	         Example
# +	        Addition	     10 + 5
# -	        Subtraction	     10 - 5
# *	        Multiplication	 10 * 5
# /	        Division	     10 / 5
# //	    Floor Division	 10 // 3
# %	        Remainder	     10 % 3
# **	    Power	         2 ** 3

# Question 11 — Basic Arithmetic

a = 20
b = 6

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Question 12 — Predict the Output

a = 17
b = 5

print(a / b)
print(a // b)
print(a % b)

#output
# 3.4
# 3
# 2

# Question 13 — Operator Precedence

result = 10 + 5 * 2
print(result)

#output
# 20

# Question 14 — More Precedence Practice

result = 20 - 4 * 3 + 2
print(result)

#output
# 6

# Question 15 — Power Operator

print(2 ** 3)
print(3 ** 2)
print(10 ** 2)

#output
# 8
# 9
# 100

side = 5
area=side**2
print(area)

# Question 16 — Shopping Bill

notebook=80
pen=20
pencile=10

total_amount=notebook+pen+pencile
print(total_amount)

# Question 17 — Multiple Quantities

note_book_cost=3*50
print("Notebook Cost :",note_book_cost)
pen_cost=2*15
print("Pen Cost :",pen_cost)
calculator_cost=500
print("Calculator Cost :",calculator_cost)

total_bill=note_book_cost+pen_cost+calculator_cost

print("Total Bill:",total_bill)

# Question 18 — Complete Groups and Remainder

student=47

complete_group=student//5
student_left=student%5

print("Complete Group:",complete_group)
print("Student Left:",student_left)

# Question 19 — Average Marks

python=85
maths=78
physics=92

total=python+maths+physics
average=total/3
print("Total:",total)
print("Average:",average)

# Question 20 — Percentage

english=78
maths=85
python=92
physics=81
chemistry=74

total=english+maths+python+physics+chemistry

percentage=(total/500)*100

print(total)
print(percentage)

# Topic 3: Digit Extraction using % and //

# Instructions
# For these questions, do not convert the number into a string.

# Use arithmetic operators.

# Question 21 — Ones Digit

number=583
ones_digit=(number%100)%10
print(ones_digit)

# Question 22 — Tens Digit

number=583
tens_digit=(number%100)//10
print(tens_digit)

# Question 23 — Hundreds Digit

number=583
hundred_digit=number//100
print(hundred_digit)

# Question 24 — Three-Digit Number Analyzer

number=746
hundred_digit=number//100
tens_digit=(number%100)//10
ones_digit=(number%100)%10
print("Ones Digit:",ones_digit)
print("Tens Digit:",tens_digit)
print("Hundreds Digit:",hundred_digit)

# Question 25 — Four-Digit Number

number=5829
thousand_digit=number//1000
hundred_digit=(number%1000)//100
tens_digit=((number%1000)%100)//10
ones_digit=((number%1000)%100)%10

print("Ones digit",ones_digit)
print("Tens digit",tens_digit)
print("Hundred digit",hundred_digit)
print("Thousand digit",thousand_digit)

# Question 26 — Sum of Digits

number=583
hundred_digit=number//100
tens_digit=(number%100)//10
ones_digit=(number%100)%10

sum=hundred_digit+tens_digit+ones_digit

print("Sum of digits",sum)

# Question 27 — Four-Digit Sum

number=4726
thousand_digit=number//1000
hundred_digit=(number%1000)//100
tens_digit=((number%1000)%100)//10
ones_digit=((number%1000)%100)%10

sum=thousand_digit+hundred_digit+tens_digit+ones_digit

print("Sum of digits",sum)

# Question 28 — Product of Digits

number=234
hundred_digit=number//100
tens_digit=(number%100)//10
ones_digit=(number%100)%10

product=hundred_digit*tens_digit*ones_digit

print("Product of Digits:",product)

# Question 29 — Reverse a Three-Digit Number

number=583
hundred_digit=number//100
tens_digit=(number%100)//10
ones_digit=(number%100)%10

reverse_digit=(ones_digit*100)+(tens_digit*10)+hundred_digit

print("Original Number:",number)
print("Reversed Number:",reverse_digit)

# Question 30 — Reverse a Four-Digit Number

number=4726
thousand_digit=number//1000
hundred_digit=(number%1000)//100
tens_digit=((number%1000)%100)//10
ones_digit=((number%1000)%100)%10

reverse_digit=(ones_digit*1000)+(tens_digit*100)+(hundred_digit*10)+thousand_digit

print("Original Number:",number)
print("Reversed Number:",reverse_digit)

# Question 31 — Place Value

number=5834
thousand_digit=number//1000
hundred_digit=(number%1000)//100
tens_digit=((number%1000)%100)//10
ones_digit=((number%1000)%100)%10

print("Ones digit",ones_digit)
print("Tens digit",tens_digit*10)
print("Hundred digit",hundred_digit*100)
print("Thousand digit",thousand_digit*1000)

# Question 32 — Difference Between First and Last Digit


number=583
hundred_digit=number//100
ones_digit=(number%100)%10

difference=hundred_digit-ones_digit

print("Difference:",difference)

# Question 33 — Digit Extraction Debugging

# The program is intended to print the ones digit.

# Find the error and correct the code.

# number = 583
# ones = number / 10

# print("Ones Digit:", ones)

number = 583
ones = (number%100)%10

print("Ones Digit:", ones)

# Question 34 — Four-Digit Extraction

number=9365
thousand_digit=number//1000
hundred_digit=(number%1000)//100
tens_digit=((number%1000)%100)//10
ones_digit=((number%1000)%100)%10

print("Thousand digit",thousand_digit)
print("Hundred digit",hundred_digit)
print("Tens digit",tens_digit)
print("Ones digit",ones_digit)

# Question 35 — Build a Number

hundreds = 5
tens = 8
ones = 3

number=hundreds*100+tens*10+ones

print("Number:",number)

# Topic 4: Real-Life Arithmetic Problems

# Question 36 — Simple Interest

principal = 10000
rate = 5
time = 2

simple_interest = (principal*rate*time) / 100

print("Simple Interest",simple_interest)

# Question 37 — Rectangle

length = 15 
width = 8 

area=length*width
perimeter=2*(length+width)

print("Area",area)
print("Perimeter",perimeter)

# Question 38 — Circle

radius=7
pi=3.14

area=pi*radius**2

print("Area:",area)

# Question 39 — Temperature Conversion

celsius = 35

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit",fahrenheit)

# Question 40 — Time Conversion

video_length=367
minutes=video_length//60*60
second=video_length%60

print("Minutes",minutes)
print("Second",second)

# Question 41 — Hours, Minutes and Seconds

total_seconds = 7384

hours=total_seconds//3600
remaining_second=total_seconds%3600
minutes=remaining_second//60
second=remaining_second%60

print("Hours",hours)
print("Minutes",minutes)
print("Second",second)


# Question 42 — Salary Calculation

basic_salary=25000
hra=5000
travel_allowance=2500
tax_deduction=3000


print("Gross Salary:",basic_salary)
net_salary=basic_salary-(hra+travel_allowance+tax_deduction)

print("Net salary:",net_salary)

# Question 43 — Travel Cost

distance=120
vehicle_gives=20

fuel_required=distance/vehicle_gives
total_fuel_cost=fuel_required*100

print("Fuel required:",fuel_required)
print("Total fuel cost:",total_fuel_cost)

# Question 44 — Shopping Discount

price = "2500"
discount = "10"

discount_price=int(price)*int(discount)/100

print("Discount amount:",discount_price)

final_price=int(price)-discount_price

print("Final price:",final_price)

# Topic 5: Type Casting + Arithmetic Operators

# Question 45 — String Numbers

price = "1200"
quantity = "4"
total_price=int(price)*int(quantity)

print(int(price))
print(int(quantity))
print("Total Price:",total_price)


# Question 46 — Student Result

python_marks = "85"
math_marks = "78"
physics_marks = "91"

total_marks=python_marks+math_marks+physics_marks
average_marks=total_marks/3

print("Total Marks",total_marks)
print("Average marks",average_marks)

# Question 47 — Bill with Tax

price = "1500"
quantity = "2"
tax_rate = "5"

p = float(price)
q = int(quantity)
t = float(tax_rate)

subtotal = p * q
tax_amount = (subtotal * t) / 100
final_bill = subtotal + tax_amount

print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

# Question 48 — Discount + GST

cost = 2000
discount_rate = 15
gst_rate = 18

discount_amount = (cost * discount_rate) / 100
price_after_discount = cost - discount_amount
gst_amount = (price_after_discount * gst_rate) / 100
final_price = price_after_discount + gst_amount

print("Discount Amount:", discount_amount)
print("Price after Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)

# Question 49 — Debug the Billing Program
price = "500"
quantity = 3
total = int(price) * quantity
print("Total:", total)


# Question 50 — Debug the Marks Program
marks1 = "80"
marks2 = "75"
marks3 = "90"
total = int(marks1) + int(marks2) + int(marks3)
print("Total Marks:", total)

# Topic 6: Output Prediction and Conceptual Practice


# Question 51 — Type Casting Output
a = "50"
b = int(a)

print(a)
print(b)
print(type(a))
print(type(b))
# Output:
# 50
# 50
# <class 'str'>
# <class 'int'>


# Question 52 — Float to Integer
number = 99.99
result = int(number)

print(number)
print(result)
# Output:
# 99.99
# 99
# Explanation: int() performs truncation, discarding the decimal without rounding.

# Question 53 — Arithmetic Output
a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# Output:
# 17
# 7
# 60
# 2.4
# 2
# 2

# Question 54 — Parentheses Challenge
print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))
# Output:
# 20
# 30
# 7.0
# 2.5
# Explanation: Parentheses override default PEMDAS/BODMAS precedence, forcing expressions
# enclosed inside them to evaluate before standard multiplication/division operations.

# Question 55 — Digit Challenge
number = 684

a = number % 10
b = number // 10
c = b % 10
d = number // 100

print(a)
print(c)
print(d)
# Output:
# 4
# 8
# 6
# Identity:
# a represents the Ones digit.
# c represents the Tens digit.
# d represents the Hundreds digit.

# Topic 7: Mixed Debugging

# Question 56 — Debug the Student Program
student_name = "Ravi"
marks = "85"
total = int(marks) + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))

# Question 57 — Debug the Number Program
number = 746
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)

# Question 58 — Debug the Discount Program
price = "2000"
discount = "15"

p = float(price)
d = float(discount)

discount_amount = p * d / 100
final_price = p - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)


# Question 59 — Complete Debugging Challenge
student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

total = int(marks1) + int(marks2) + int(marks3)
average = total / 3

print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))



# Question 60 — Final Challenge: Number + Billing

# --- Part A: Number Analysis ---
number = 5836

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

sum_of_digits = thousands_digit + hundreds_digit + tens_digit + ones_digit
reversed_number = (ones_digit * 1000) + (tens_digit * 100) + (hundreds_digit * 10) + thousands_digit

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)
print("Sum of Digits:", sum_of_digits)
print("Reversed Number:", reversed_number)

# --- Part B: Product Billing ---
price = "1250"
quantity = "4"
discount = "10"

p = float(price)
q = int(quantity)
d = float(discount)

subtotal = p * q
discount_amount = (subtotal * d) / 100
final_amount = subtotal - discount_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)



