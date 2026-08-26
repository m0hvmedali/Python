# map(function, iterable) هنا القصد انك بتاخد كل عنصر في ال iterable وبتطبق عليه 
# the same function مش بتغير حاجة
# map(function, iterable) => map(do_what, on_what)
Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
# وانا عايز اخد كل رقم واضربه في 2 الطريقه الاولى
# way 1:
for number in Num :
    result.append(number * 2)
print(result)
print('#'*40)
# output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# way2:
result = map(lambda number:number * 2,Num)
print(list(result))
print('#'*40)
# output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# way 3: 
def squar(number):
    return number * number
# نستخدم الماب لتطبيق الدالة على كل عنصر
result = map(squar,Num)
print(list(result))
# output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('#'*40)
#######################################################
# MAP
# كل عنصر ──→ function ──→ نتيجة جديدة
#    1      ──→ ×2      ──→ 2
#    2      ──→ ×2      ──→ 4
#    3      ──→ ×2      ──→ 6
########################################################
# FILTER
# كل عنصر ──→ function ──→ True/False
#    1      ──→ is_even ──→ False ❌
#    2      ──→ is_even ──→ True  ✅
#    3      ──→ is_even ──→ False ❌
#    4      ──→ is_even ──→ True  ✅

# Example 1

def checkNumber(num):

  return num > 10

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)

for number in myResult:

  print(number)

print("#" * 40)

# Example 2

def checkName(name):

  return name.startswith("O")

myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myTexts)

for person in myReturnedData:

  print(person)

print("#" * 40)

# Example 3

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

for p in filter(lambda name: name.startswith("A"), myNames):

  print(p)
