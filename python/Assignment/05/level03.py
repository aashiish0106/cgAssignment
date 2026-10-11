# Q15. Factorial of a Number

n=int(input("Enter the value of N: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)

# Q16. Factorial from 1 to N

n=int(input("Enter the value of N: "))
count=1
for i in range(1,n+1):
    count=count*i
    print(f"{i}! = {count}")

# Q17. Product of Even Numbers

n=int(input("Enter the value of N: "))
product=1
for i in range(2,n+1):
    if i%2==0:
        product=product*i
print(product)

# Q18. Product of Odd Numbers

n=int(input("Enter the value of N: "))
product=1
for i in range(1,n+1):
    if i%2!=0:
        product=product*i
print(product)

# Q19. Double Factorial — Even Numbers

n=int(input("Enter the value of N: "))
product=1
for i in range(2,n+1):
    if i % 2 == 0 :
        product=product*(i)
print(product)

# Q20. Sum of Squares

n=int(input("Enter the value of N: "))

sum_of_square=0
for i in range(1,n+1):
    sum_of_square=sum_of_square+i**2
print(sum_of_square)


# Q21. Sum of Cubes

n=int(input("Enter the value of N: "))

sum_of_cubes=0
for i in range(1,n+1):
    sum_of_cubes=sum_of_cubes+i**3
print(sum_of_cubes)


# Q22. Factorial-Based Sum

n=int(input("Enter the value of N: "))

factorial=1
factorial_sum=0

for i in range(1,n+1):
    factorial=factorial*i
    factorial_sum=factorial_sum+factorial

print(factorial_sum)


