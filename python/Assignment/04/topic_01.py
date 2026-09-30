# Topic-1 — Basic if Statements

# Q1. Positive Number
num=int(input("Enter a number: "))
if num>0:
    print("Positive Number")

# Q2. Voting Eligibility Check
age=int(input("Enter your Age: "))
if age>=18:
    print("Eligible to vote")

# Q3. Temperature Warning

temp=int(input("Enter the temperature: "))
if temp>40:
    print("High Temperature")

# Q4. Divisible by 5

num=int(input("Enter a number for checking the divisibility by 5: "))
if num%5==0 :
    print("Divisible by 5")

# Q5. Free Delivery

amount=int(input("Enter the amount: "))
if amount>=1000:
    print("Free Delivery")

# Q6. Character Check

character=input("Enter a character: ")
if character=="A":
    print("You entered A")

# Q7. Password Length Check

password=input("Enter your password: ")
if len(password)>=8:
    print("Strong Length")

# Q8. Number of Digits

num=int(input("Enter a number: "))
if num>=100 and num<=999 :
    print("Three Digit Number")


