# Topic-11 — Integrated Problems

# Q60. Student Result Information

# name=input("Enter your name:")
# python,js,cpp=input("Enter your 3 subject marks with space").split()
# total=int(python)+int(js)+int(cpp)
# avg=total/3

# print(f"Name: {name}\nTotal: {total}\nAverage: {avg}")

# Q61. Student ID Analyzer

id="BTECH-24-CSE-105"
degree,batch,branch,roll=id.split("-")

print(f"Degree: {degree}\nBatch: {batch}\nBranch: {branch}\nRoll Number: {int(roll)}")

last_three =id[-3:]
print(last_three)

# Q62. Username Generator

full_name = input()
first, middle, last = full_name.split()
username = f"{first.lower()}.{last.lower()}"
print(username)

# Q63. Sentence Information

sentence = "Python is very powerful"
first, second, third, last = sentence.split()
print(f"First word: {first}")
print(f"Last word: {last}")
print(len(sentence.split()))

# Q64. Email Analyzer + Membership

email = input()
at_present = "@" in email
username_part, domain_part = email.split("@")
print(f"@ Present: {at_present}")
print(f"Username: {username_part}")
print(f"Domain: {domain_part}")

# Q65. Character Analyzer

char = input()
code = ord(char)
prev_char = chr(code - 1)
next_char = chr(code + 1)
print(f"Character: {char}")
print(f"Code: {code}")
print(f"Previous: {prev_char}")
print(f"Next: {next_char}")

# Q66. Product Bill

product = input()
price = float(input())
quantity = int(input())
discount_percentage = float(input())
subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount
print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")

# Q67. Date Analyzer

date_str = input()
day, month, year = date_str.split("-")
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(date_str[-4:])

# Q68. String Transformation Challenge

text = "Python Programming"
word1, word2 = text.split()
print(f"First Word: {word1}")
print(f"Second Word: {word2}")
print(f"First Word Reversed: {word1[::-1]}")
print(f"Second Word Reversed: {word2[::-1]}")

# Q69. Final Challenge — Student Code Formatter

code_id = input()
degree, batch, branch, roll = code_id.split("-")
code_formatted = f"{degree}/{branch}/{roll}"
print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {code_formatted}")

# Q70. Final String + Input/Output Challenge

name_input = input()
first_name, middle_name, last_name = name_input.split()
first_upper = first_name[:3].upper()
last_lower = last_name[:3].lower()
reversed_full = name_input[::-1]
print(f"Original: {name_input}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper}")
print(f"Last Name (Lower Part): {last_lower}")
print(f"Full Name Reversed: {reversed_full}")