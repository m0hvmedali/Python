# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# -----------------------------------------------

"""
This is My Module
To Create Function
To Say Hello
"""
def say_hello(name):
  '''This Function Only Say Hello To Someone'''
  msg = "Hello"
  return f"{msg} {name}"

say_hello("Ahmed")

# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

x = -10

if x < 0:

  raise Exception(f"The Number {x} Is Less Than Zero")

  print("This Will Not Print Because The Error")

else:

  print(f"{x} Is Good Number and Ok")

print('Print Message After If Condition')

y = 10

if type(y) != int:

  raise ValueError("Only Numbers Allowed")

print('Print Message After If Condition')

# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

number = int(input("Write Your Age: "))

print(number)
print(type(number))

try:  # Try The Code and Test Errors

  number = int(input("Write Your Age: "))

  print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors

  print("Good, This Is Integer From Else")

finally:

  print("Print From Finally Whatever Happens")


try:

  # print(10 / 0)
  # print(x)
  print(int("Hello"))

except ZeroDivisionError:

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Elzero")

except:

  print("Error Happens")


  # -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------

the_file = None

the_tries = 5

while the_tries > 0:

  try:  # Try To Open The File

    print("Enter The File Name With Absolute Path To Open")

    print(f"You Have {the_tries} Tries Left")

    print("Example: D:\Python\Files\yourfile.extension")

    file_name_and_path = input("File Name => : ").strip()

    the_file = open(file_name_and_path, 'r')

    print(the_file.read())

    break

  except FileNotFoundError:

    print("File Not Found Please Be Sure The Name is Valid")

    the_tries -= 1

  except:

    print("Error Happen")

  finally:

    if the_file is not None:

      the_file.close()

      print("File Closed.")

else:

  print("All Tries Is Done")

  

