# 1. الدالة enumerate() 
names = ["Mohamed", "Ahmed", "Ali"]
#  وعايز اطبع العنصر ومعاه رقمه اللي هو ال index بتاعه 
# اول طريقه 
for i in range(len(names)):
    print(f"{i+1} : {names[i]}")
print('#'*40)
##########################################
# تاني طريقه 
for index, name in enumerate(names):
    print(f"{index+1} : {name}")
print('#'*40)
##########################################
# تالت طريقه 
for index, name in enumerate(names,10):
    print(f"{index+1} : {name}")
print('#'*40)
##########################################
# 2. الدالة helper()
print(help(enumerate))
print('#'*40)
##########################################
# 3. الدالة reversed()
names = ["Mohamed", "Ahmed", "Ali"]
for name in reversed(names):
    print(name)
##########################################
# 4. الدالة bin()
number = 10
print(bin(number))
print('#'*40)
##########################################
# 5. الدالة id()
name = "Mohamed"
print(id(name))
##########################################
# 6. الدالة abs()
number = -10
print(abs(number))
##########################################
# 7. الدالة pow()
number = 10
power = 2
print(pow(number, power))
##########################################
# 8. الدالة min()
numbers = [1, 2, 3, 4, 5]
print(min(numbers))
##########################################
# 9. الدالة max()
numbers = [1, 2, 3, 4, 5]
print(max(numbers))
##########################################
# 10. الدالة slice()
numbers = [1, 2, 3, 4, 5]
print(slice(numbers, 1, 3))
##########################################
# 11. الدالة round()
number = 10.5
print(round(number))
##########################################
# 12. الدالة range()
numbers = range(10)
print(list(numbers))
##########################################
# 13. الدالة sum()
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

