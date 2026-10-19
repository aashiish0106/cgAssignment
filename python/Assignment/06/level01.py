# Level 1 — Basic Patterns

# Q1. Solid Square

n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

# Q2. Solid Rectangle

rows = 3
columns = 6

for i in range(rows):
    for j in range(columns):
        print("*",end="")
    print()

# Q3. Increasing Star Triangle

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

# Q4. Increasing Number Triangle

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Q5. Repeated Number Triangle

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

# Q6. Repeated Alphabet Triangle

s="ABCDE"
for i in range(len(s)):
    for j in range(i+1):
        print(s[i],end="")
    print()

# Q7. Alphabet Triangle

s="ABCDE"
for i in range(len(s)):
    for j in range(i+1):
        print(s[j],end="")
    print()

# Q8. Continuous Number Triangle

n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Q9. Alternating 0–1 Triangle

# n=5
# num=1

# for i in range(n):
#     num = 1 if i % 2 == 0 else 0 
#     for j in range(i+1):
#         print(num,end="")
#         if num==1:
#             num=0
#         elif num==0:
#             num=1
    
#     print()


n=5
num=1
for i in range(n):
    num = 1 if i % 2 == 0 else 0 
    for j in range(i+1):
        print(num,end="")
        num = 1 - num
    print()

# Q10. Decreasing Star Triangle

n=5

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

# Q11. Decreasing Number Triangle

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Q12. Decreasing Alphabet Triangle

s="ABCDE"
for i in range(len(s),0,-1):
    for j in range(i):
        print(s[j],end="")
    print()



