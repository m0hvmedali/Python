import re
# print(dir(re))
# print(re.__version__)
# training on patterns

text = """
Ahmed: 01012345678
Mohamed: 011-2345-6789
Sara: +2010123456789
Omar: 012 3456 7890
Invalid: 123456
Another: 01598765432
"""
# pattern =  r"(\+20|01)[- ]?[0-9]{10}\b"
pattern =  r"(\+20|01)\d{8}\d{8}"
print(re.findall(pattern, text))

# \b means word boundary 
# ^ means start of the string
# $ means end of the string
# . means any character
# * means zero or more
# + means one or more
# ? means zero or one
# [] means any of these characters
# () means group
# | means or
# \d means digit
# \w means word character
# \s means space character
# \b means word boundary
# \B means not a word boundary
# \t means tab
# \n means newline
# \r means carriage return
# \f means form feed
# \v means vertical tab
# \a means alert
# \b means backspace
# \e means escape
