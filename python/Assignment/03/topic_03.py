# Topic-3 — Membership Operators with Strings

# Q7. Basic Membership

text = "Python Programming"

print("Python" in text)#True
print("Java" in text)#False
print("Python" not in text)#False

# Q8. Character Membership

word = "computer"

print("p" in word)
print("x" in word)
print("c" not in word)


# Q9. Case Sensitivity in Membership

text = "Python"

print("P" in text)#True
print("p" in text)#False
print("Python" in text)#True
print("python" in text)#False

#some results are different because pyton is a case sensetive language 

# Q10. Membership with User Input

word=input("Enter a word or sentence:")

print("a" in word)

# Q11. Email Symbol Check

email=input("Enter an email:")

print("a" in email)

