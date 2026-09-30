# Q44. Greatest of Three Numbers
a, b, c = map(int, input().split())

if a == b and b == c:
    print("All are Equal")
elif a >= b and a >= c:
    if a == b:
        print("A and B are Equal and Greatest")
    elif a == c:
        print("A and C are Equal and Greatest")
    else:
        print("A is Greatest")
elif b >= a and b >= c:
    if b == a:
        print("A and B are Equal and Greatest")
    elif b == c:
        print("B and C are Equal and Greatest")
    else:
        print("B is Greatest")
else:
    if a == c:
        print("A and C are Equal and Greatest")
    elif b == c:
        print("B and C are Equal and Greatest")
    else:
        print("C is Greatest")

# Q45. Student Result with Grade
marks, attendance = map(int, input().split())

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")

# Q46. Employee Bonus
inputs = input().split()
salary = float(inputs[0])
rating = int(inputs[1])

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")

# Q47. Bus Ticket Category
inputs = input().split()
age = int(inputs[0])
distance = float(inputs[1])

if age < 5:
    print("Free")
elif age <= 59:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")
else:
    print("Senior")

# Q48. Product Purchase Validation
inputs = input().split()
stock = int(inputs[0])
payment = inputs[1]

if stock > 0:
    if payment == "paid":
        print("Order Confirmed")
    elif payment == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")

# Q49. Travel Ticket Validation
inputs = input().split()
age = int(inputs[0])
ticket_type = inputs[1]

if age < 5:
    print("Free Travel")
elif age <= 59:
    if ticket_type == "AC":
        print("AC Ticket")
    elif ticket_type == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
else:
    print("Senior Passenger")

