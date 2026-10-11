import math

# # Q23. Count Digits Using a Loop

# n=int(input("Enter a Number: "))
# digit=int(math.log10(n))+1
# count=0
# for i in range(digit):
#     count=count+1
# print(count)

# # Q24. Sum of Digits

# num=int(input("Enter a Number: "))
# digit=int(math.log10(num))+1
# sum=0
# for i in range(digit):
#     sum=sum+num%10
#     num=num//10
# print(sum)

# # Q25. Product of Digits

# num=int(input("Enter a Number: "))
# digit=int(math.log10(num))+1
# sum=1
# for i in range(digit):
#     sum=sum*num%10
#     num=num//10
# print(sum)

# # Q26. Count Even Digits

# num=int(input("Enter a Number: "))
# digit=int(math.log10(num))+1
# count=0

# for i in range(digit):
#     if (num%10)%2==0:
#         count=count+1
#     num=num//10

# print(count)

# # Q27. Sum of Even Digits

# num=int(input("Enter a Number: "))
# digit=int(math.log10(num))+1
# sum=0

# for i in range(digit):
#     if (num%10)%2==0:
#         sum=sum+(num%10)
#     num=num//10

# print(sum)

# # Q28. Largest Digit Without max()

# num=int(input("Enter the a Number: "))
# digit=int(math.log10(num))+1
# largest=0
# for i in range(digit):
#     if num%10>largest:
#         largest=num%10
#     num=num//10
# print(largest)

# # Q29. Smallest Digit Without min()

# num=int(input("Enter the a Number: "))
# digit=int(math.log10(num))+1
# smallest=10
# for i in range(digit):
#     if num%10<smallest:
#         smallest=num%10
#     num=num//10
# print(smallest)

# Q30. Reverse a Number

# num=int(input("Enter the Number: "))
# digit=int(math.log10(num))+1
# rev=0
# for i in range(digit):
#     rev=rev+num%10
#     rev=rev*10
#     num=num//10
# rev=rev//10
# print(rev)

# Q31. Palindrome Number

# num=int(input("Enter the Number: "))
# pallindrome_check=num
# digit=int(math.log10(num))+1
# rev=0
# for i in range(digit):
#     rev=rev+num%10
#     rev=rev*10
#     num=num//10
# rev=rev//10
# if rev==pallindrome_check:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Q32. Count a Specific Digit

# num=int(input("Enter a Number: "))
# digit=input("Enter the digit to count: ")
# check_num=str(num)
# count=0

# for i in check_num:
#     if i==digit:
#         count=count+1
# print(count)

# Q33. First Digit Using Repeated Division

# n=int(input("Enter a Number: "))
# digit=int(math.log10(n))+1
# for i in range(digit):
#     n=n//10
#     if n>0 and n<10:
#         print(n)

# Q34. Difference Between Largest and Smallest Digit

# n=int(input("Enter a Number: "))
# digit=int(math.log10(n))+1
# max=0
# min=10
# for i in range(digit):
#     if n%10>max:
#         max=n%10
#     if n%10<min:
#         min=n%10
#     n=n//10
# print(max)
# print(min)
# print(max-min)

# Q35. Digit Position Value
n=int(input("Enter a Number: "))
digit=int(math.log10(n))+1

for i in range(1,digit+1):
    print(n%10,i)
    n=n//10







