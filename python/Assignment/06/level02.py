# Level 2 — Spaces and Alignment

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# Q14. Inverted Right-Aligned Half Pyramid

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# Q15. Star Pyramid

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

# Q16. Inverted Star Pyramid

# n=5
# for i in range(n,0,-1):
#     for k in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# Q17. Solid Diamond

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()
# n=n-1
# for i in range(n,0,-1):
#     for j in range((n-i)+1):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()


# Q18. Rhombus

# n=5
# for i in range(5):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(n):
#         print("*",end="")
#     print()

# Q19. Mirrored Number Pattern

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(2*n-2*i):
#         print(" ",end="")
#     for l in range(i,0,-1):
#         print(l,end="")
#     print()

    
# Q20. Centered Number Pyramid

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()

# Q21. Palindromic Number Pyramid

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     if i>1:
#         for k in range(i-1,0,-1):
#             print(k,end="")
#     print()

# 22. Alphabet Palindrome Pyramid

s="ABCDE"
for i in range(len(s)):
    for j in range(len(s)-(i+1),0,-1):
        print(" ",end="")
    for k in range(i+1):
        print(s[k],end="")
    if i>0:
        for l in range(i,-1,-1):
            print(s[l],end="")
    print()
