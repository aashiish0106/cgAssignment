# Topic-7 — String split()

# Q33. Basic split()
text = "Python is easy"

print(text.split())#["Python","is","easy"]

# Explain what separates the words.
#Ans-" " seperates the words

# Q34. Custom Separator

data = "apple,banana,mango"

print(data.split(","))#["apple","banana","mango"]

# Q35. Separator Not Present

text = "Python is easy"

print(text.split(","))#['Python is easy']

# Why does it not split at the spaces?
# Ans-Because there is no "," 



# Q36. Split a Full Name

name="Rahul Kumar Sharma"

first,middle,last=name.split()
print(first)
print(middle)
print(last)

# Q37. Multiple Inputs Using split()

name=input("Enter your name ").split()
first_name,last_name=name
print(f"First Name:{first_name}")
print(f"Last Name:{last_name}")

# Q38. Three Numeric Inputs

nums=input("Enter three number with space").split()
a,b,c=nums
sum=int(a)+int(b)+int(c)
print(f"Sum:{sum}")

# Q39. Student Record

info="Rahul,20,BTech,Ahmedabad"
name,age,course,city=info.split(",")

print(f"Name:{name}")
print(f"Age:{age}")
print(f"Course:{course}")
print(f"City:{city}")

# Q40. Email Analyzer

email=input("Enter an email with @:")
username,domain=email.split("@")

print(f"UserNmae:{username}")
print(f"Domain:{domain}")

# Q41. Sentence Analyzer

sentence=input("Enter your Sentence")
words=sentence.split()
print(f"First word:{words[0]}")
print(f"Last word:{words[-1]}")
