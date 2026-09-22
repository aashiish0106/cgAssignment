# Topic-10 — Debugging

# Q54. String and Integer

# age = input("Enter age: ")
# print("Age after 5 years:", age + 5)

age = int(input("Enter age: "))
print("Age after 5 years:", age + 5)

# Q55. Incorrect Quotes

# print('It's Python')

print('It\'s Python')

# Q56. Incorrect Slicing Syntax

# text = "Python"
# print(text[1,4])

text = "Python"
print(text[1:4])

# Q57. Incorrect split() Separator

# a, b = input().split(",")

a, b = input().split(" ")

# Q58. String Addition vs Numeric Addition

# a, b = input().split()

# print(a + b)

a,b = input().split()

print(int(a) + int(b))

# Q59. Escape Sequence Debugging

# print("C:\new\test")

print("C:\\new\\test")

