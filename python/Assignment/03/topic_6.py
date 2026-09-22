# Topic-6 — String Slicing

# Q24. Basic Slicing

text = "PYTHON"

print(text[0:3])#PYT
print(text[2:5])#THO
print(text[1:6])#YTHON

# Q25. Start and Stop

text = "PROGRAMMING"

print(text[:4])#PROG
print(text[4:])#RAMMING
print(text[:])#PROGRAMMING

# Q26. Negative Slicing

text = "COMPUTER"

print(text[-5:])#PUTER
print(text[:-3])#COMPU
print(text[-6:-2])#MPUT

# Q27. Step in Slicing

text = "PYTHON"

print(text[::2])#PTO
print(text[1::2])#YHN
print(text[::-1])#NOHTYP

# Q28. Reverse a String

text=input("Enter a string:")
print("Reversed:",text[::-1])

# Q29. Alternate Characters

text=input("Enter a string:")
print("Alternate string:",text[::2])

# Q30. Extract First and Last Three Characters

text=input("Enter a string:")

print(f"First Three character{text[0:4]}")
print(f"Last Three character{text[-1:-5]}")

# Q31. Slicing Challenge

text = "ABCDEFGHIJ"

print(text[2:8:2])#output="CEG"
# start=2,stop=8,step=2

print(text[8:2:-2])#output="IGE"
# start=8,stop=2,step=-2

print(text[::-2])#output="JHFDB"
# start= ,stop= ,step=-2

# Q32. Slice Without Counting from the Beginning

text = "BTECH-CSE-2026"

print(text[0:5])
print(text[6:9])
print(text[10:14])

