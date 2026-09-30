# Q58. Student ID Validation

student_id = input("Enter Student ID: ")
parts = student_id.split("-")
branch = parts[2]

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")

# Q59. Email Domain Checker
email = input("Enter email address: ")
domain = email.split("@")[1]

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")

# Q60. Username Generator Validation
full_name = input("Enter full name (three words): ")
words = full_name.split()
username = words[0] + "." + words[2]

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")

# Q61. Number Digit Analyzer
num = int(input("Enter a positive integer: "))

if num < 10:
    print("One Digit")
elif num < 100:
    print("Two Digits")
elif num < 1000:
    print("Three Digits")
else:
    print("Four or More Digits")

# Q62. Shopping Bill Category
price = float(input("Enter product price: "))
qty = int(input("Enter quantity: "))

subtotal = price * qty

if subtotal >= 5000:
    discount = 20
elif subtotal >= 2000:
    discount = 10
else:
    discount = 0

final = subtotal - (subtotal * discount / 100)
print(f"Subtotal: {subtotal:.0f}, Discount: {discount}%, Final: {final:.2f}")

# Q63. Electricity Bill Category
units = int(input("Enter units consumed: "))

if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate
print(f"Units: {units}, Rate: ₹{rate}, Bill: ₹{bill}")

# Q64. ATM Menu
balance = 10000
choice = int(input("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nEnter choice: "))

match choice:
    case 1:
        print(f"Balance: {balance}")
    case 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposit Successful, Balance: {int(balance)}")
    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal Successful, Balance: {int(balance)}")
        else:
            print("Insufficient Balance")
    case 4:
        print("Exiting...")
    case _:
        print("Invalid Choice")

# Q65. Restaurant Ordering System
item = int(input("1 → Pizza (₹250)\n2 → Burger (₹150)\n3 → Pasta (₹200)\n4 → Sandwich (₹120)\nEnter choice: "))
qty = int(input("Enter quantity: "))

match item:
    case 1: price = 250
    case 2: price = 150
    case 3: price = 200
    case 4: price = 120
    case _: price = 0

if price > 0:
    total = price * qty
    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0.0
    final = total - discount
    print(f"Total: {total}, Discount: {discount:.2f}, Final: {final:.2f}")
else:
    print("Invalid Item Choice")

# Q66. Exam Result Analyzer
m1 = int(input("Subject 1 marks: "))
m2 = int(input("Subject 2 marks: "))
m3 = int(input("Subject 3 marks: "))
attendance = int(input("Attendance percentage: "))

if attendance >= 75:
    total = m1 + m2 + m3
    avg = total / 3
    if avg >= 90:
        print("Outstanding")
    elif avg >= 75:
        print("Very Good")
    elif avg >= 60:
        print("Good")
    elif avg >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")

# Q67. Cab Fare Calculator
distance = float(input("Enter distance in km: "))
ride_type = input("Enter ride type (normal/premium): ")

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0

if rate > 0:
    fare = distance * rate
    if distance > 20:
        fare += fare * 0.10
    print(f"Fare: {fare:.2f}")
else:
    print("Invalid Ride Type")

# Q68. College Admission System


# Topic-9 — Debugging Conditional Programs
