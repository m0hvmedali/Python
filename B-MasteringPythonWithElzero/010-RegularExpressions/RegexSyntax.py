import re

# task 1 :
# text = "I love Python"
# result = re.search("Python", text)
# print(result)
# taslk 2 :
# text = "The cat is sleeping"
# result = re.findall("cat", text)
# print(result)

#################################################

pattern = "[a-zA-Z]+[0-9]*"
text = input("Enter text: ")
result = re.search(pattern, text)
print(result)
# check
# INPUT: mohamed123
# Output: <re.Match object; span=(0, 10), match='mohamed123'>
