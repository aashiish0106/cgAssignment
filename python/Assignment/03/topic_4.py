# Q12. Find Character Codes

# A
print(ord("A"))
# a
print(ord("a"))
# Z
print(ord("Z"))
# z
print(ord("z"))
# 0
print(ord("0"))
# 9
print(ord("9"))
# @
print(ord("@"))

# Q13. Convert Codes to Characters

# 65
print(chr(65))
# 66
print(chr(66))
# 97
print(chr(97))
# 98
print(chr(98))
# 48
print(chr(48))
# 57
print(chr(57))
# 64
print(chr(64))

# Q14. Uppercase and Lowercase

# A
# a
print(ord("A"))
print(ord("a"))

# B
# b
print(ord("B"))
print(ord("b"))

# Which is larger: ord("A") or ord("a")?
# Ans -> a is larger because the uni code of "a" is larger than "A"

# What is the difference between them?

# Ans -> The difference is 32

# Is the difference the same for B and b?

# Ans -> Yes the difference will be the same 

# Q15. Character Code Program

character=input("Enter a character")
print("The Character code is:",ord(character))

# Q16. Next Character

input_letter=input("Enter a Single Uppercase letter")
print("The next letter is:",chr(ord(input_letter)+1))

# Q17. Character Comparison and Unicode

print("A" < "B")#True
print("a" < "b")#True
print("A" < "a")#True
print("0" < "9")#True

print(ord("A"),ord("B"),sep="<")
print(ord("a"),ord("b"),sep="<")
print(ord("A"),ord("b"),sep="<")
print(ord("0"),ord("9"),sep="<")

# Q18. Unicode Character Challenge

# 9731
chr(9731)
# 9829
chr(9829)
# 8377
chr(8377)
