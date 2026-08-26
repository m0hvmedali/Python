# intro to if conditions in python
"""
1. what is if condition in python?
in python if condetions it a flow control statement that allows you to execute a block ao code if a specified condition is true. it is used to make decisions in your code based on certain conditions.
=========================================
2. how to use if condition in python?
the basic syntax of an if condition in python is as follows: 
=========================================
3. what is the syntax of if condition in python?
if condition:
    # block of code to be executed if the condition is true
=========================================   
4. what is the syntax of if else condition in python?
if condition:
    # block of code to be executed if the condition is true
else: 
    # block of code to be executed if the condition is false
=========================================
5. what is the syntax of if elif else condition in python?
if condition1:  
    # block of code to be executed if condition1 is true
elif condition2:
    # block of code to be executed if condition2 is true
else:   
    # block of code to be executed if both condition1 and condition2 are false
=========================================
6.Ternary If it is a shorthand way of writing an if-else statement in a single line. The syntax is as follows:
value_if_true if condition else value_if_false

 """
# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

  # ---------------
# -- Nested If --
# ---------------

uName = "Osama"
isStudent = "Yes"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

  if isStudent == "Yes":

    print(f"Hi {uName} Because U R From {uCountry} And Student")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

  else:

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


elif uCountry == "Kuwait" or uCountry == "Bahrain":

  print(f"Hi {uName} Because U R From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hi {uName} Because U R From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

  # ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "A"

if country == "Egypt" : print(f"The Weather in {country} Is 15")
elif country == "KSA" : print(f"The Weather in {country} Is 30")
else : print("Country is Not in The List")

# Short If

movieRate = 18
age = 18

if age < movieRate :

  print("Movie S Not Good 4U") # Condition If True

else :

  print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False
