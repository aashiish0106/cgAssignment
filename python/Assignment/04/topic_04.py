# Q29. College Admission Eligibility

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")


# Q30. Scholarship Eligibility
marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")

# Q31. Weekend Check
day = input("Enter day name: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# Q32. Online Exam Access
username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# Q33. Delivery Availability
city = input("Enter city: ")

if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")

# Q34. Number Range Check
num = int(input("Enter an integer: "))

if num >= 10 and num <= 50:
    print("Inside Range")
else:
    print("Outside Range")

# Q35. Secure Transaction
amount = float(input("Enter transaction amount: "))
otp = input("Enter OTP: ")

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")



