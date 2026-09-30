# Topic-7 — match-case

# Q50. Basic Menu
menu_no = int(input("Enter menu number: "))

match menu_no:
    case 1:
        print("1 → Add")
    case 2:
        print("2 → View")
    case 3:
        print("3 → Update")
    case 4:
        print("4 → Delete")
    case _:
        print("Invalid Choice")

# Q51. Day Name Using match-case
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("1 → Monday")
    case 2:
        print("2 → Tuesday")
    case 3:
        print("3 → Wednesday")
    case 4:
        print("4 → Thursday")
    case 5:
        print("5 → Friday")
    case 6:
        print("6 → Saturday")
    case 7:
        print("7 → Sunday")
    case _:
        print("Invalid Day")

# Q52. Calculator Using match-case
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print(f"{num1} + {num2} → {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} → {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} → {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} → {num1 / num2}")
        else:
            print("Division by zero error")
    case _:
        print("Invalid Operator")


# Q53. Traffic Signal Using match-case
signal = input("Enter traffic signal color: ").strip().lower()

match signal:
    case "red":
        print("red → Stop")
    case "yellow":
        print("yellow → Wait")
    case "green":
        print("green → Go")
    case _:
        print("Invalid Signal")

# Q54. Grade Message Using match-case
grade = input("Enter grade: ").strip().upper()

match grade:
    case "A":
        print("A → Excellent Performance")
    case "B":
        print("B → Very Good Performance")
    case "C":
        print("C → Good Performance")
    case "D":
        print("D → Needs Improvement")
    case "F":
        print("F → Failed")
    case _:
        print("Invalid Grade")

# Q55. Mobile Service Menu
code = int(input("Enter service code: "))

match code:
    case 1:
        print("1 → Check Balance")
    case 2:
        print("2 → Recharge")
    case 3:
        print("3 → Data Usage")
    case 4:
        print("4 → Customer Support")
    case _:
        print("Invalid Service")

# Q56. Month Name Using match-case
month = int(input("Enter month number (1-12): "))

match month:
    case 1:
        print("1 → January")
    case 2:
        print("2 → February")
    case 3:
        print("3 → March")
    case 4:
        print("4 → April")
    case 5:
        print("5 → May")
    case 6:
        print("6 → June")
    case 7:
        print("7 → July")
    case 8:
        print("8 → August")
    case 9:
        print("9 → September")
    case 10:
        print("10 → October")
    case 11:
        print("11 → November")
    case 12:
        print("12 → December")
    case _:
        print("Invalid Month")

# Q57. File Type Detector
ext = input("Enter file extension: ").strip().lower()

match ext:
    case "py":
        print("py → Python File")
    case "txt":
        print("txt → Text File")
    case "pdf":
        print("pdf → PDF File")
    case "jpg":
        print("jpg → Image File")
    case _:
        print("Unknown File Type")