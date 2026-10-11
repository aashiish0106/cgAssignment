# Level 2 — Counting & Accumulation

# Q7. Sum of Numbers in a Range

start=int(input("Enter the value of start: "))
end=int(input("Enter the value of end: "))
sum=0
for i in range(start,end+1):
    sum=sum+i
print(sum)

# Q8. Count Multiples of 3

n=int(input("Enter the value of N: "))
count=0
for i in range(1,n+1):
    if i%3==0:
        count=count+1
print(count)

# Q9. Sum of Multiples of 4

n=int(input("Enter the value of N: "))
sum=0
for i in range(1,n+1):
    if i%4==0:
        sum=sum+i
print(sum)

# Q10. Count Numbers with Two Conditions

n=int(input("Enter the value of N: "))
count=0
for i in range(1,n+1):
    if i%3==0 and i%5==0 :
        count=count+1
print(count)

# Q11. Sum Numbers Except Multiples of 3

n=int(input("Enter the value of N: "))
sum=0
for i in range(1,n+1):
    if i%3!=0 :
        sum=sum+i
print(sum)

# Q12. Count Even and Odd Together

n=int(input("Enter the value of N: "))
even=0
odd=0

for i in range(1,n+1):
    if i%2==0:
        even=even+1
    else :
        odd=odd+1
print(f"Even = {even},Odd = {odd}")

# Q13. Running Sum

n=int(input("Enter the value of N: "))
count=0
for i in range(1,n+1):
    count=count+i
    print(count)

# Q14. Running Product

n=int(input("Enter the value of N: "))
count=1
for i in range(1,n+1):
    count=count*i
    print(count)






