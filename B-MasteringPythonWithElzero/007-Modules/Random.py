import random
print(dir(random))
# show all func in this module
print('#'*40)
###########################
# random is a module in paython: اختيار شبه عشوائي
# randint(a, b) is a function in random: اختيار عدد صحيح عشوائي بين a و b
r = random.randint(1,100)
print(r) 
print('#'*40)
###########################
names= ["mohammed","ali","osama","ahmed","omran"]
pick_one = random.choice(names)
print(pick_one)
print('#'*40)
###########################
# خلط عشوائي ل عناصر القائمه باستخدام داله shuffle
cards =[1,2,3,4,5,6,7,8,9,10,'A','J','Q','K']  
random.shuffle(cards)
print(cards)    
print('#'*40)
###########################
# random.random() is a function in random: اختيار عدد عشري عشوائي بين 0 و 1
print(random.random())    
print('#'*40)
###########################
# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random
print(random)
print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
print(dir(random))

# Import One Or Two Functions From Module
from random import randint, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")

# <md>
# \# Algorithm Optimization
# This function implements the gradient descent update:
# $$ \theta_{j} := \theta_{j} - \alpha \frac{\partial}{\partial \theta_{j}} J(\theta) $$
#
# </md>
