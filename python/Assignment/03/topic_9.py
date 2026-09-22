# Topic-9 — print(), sep, end, and f-Strings

# Q49. sep

print("2026", "09", "09", sep="-")
# 2026-09-09

# Q50. end

print("Hello", end=" ")
print("Python")

# Hello Python 

# Q51. sep and end

print("10","20","30",sep="-",)
print("40","50","60",sep="-")

# print("10","20","30"," ","40","50","60",sep="-",end=" ")

name=input("Enter your name:")
age=int(input("Enter your age:"))
city=input("Enter your city")
course=input("Enter your course")

print(f"Name: {name}\nAge: {age}\nCity: {city}\nCourse:{course}")

# Q53. Formatted Price

price = float(input())

print(f"{price:.2f}")





