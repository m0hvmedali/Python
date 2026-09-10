from collections import abc
# ╭──────────────╮
# │ [List comps] │
# ╰──────────────╯
# TODO: convert to list comps
# NOTE: [expression for item in iterable if condition]
result = []

for x in range(1, 11):
    result.append(x ** 2)
# -----
result = [x**2 for x in range(1,11)]
print (result)
# ══════════════════════════════════════════════════════════════════════════════
result = []
for x in range(1, 21):
    if x % 2 == 0:
        result.append(x)
# ----
result =[x for x in range(1,21) if x % 2 ==0]
print (result)
# # ══════════════════════════════════════════════════════════════════════════════
result =[x for x in range(1,21) if x % 2 !=0]
print (result)
# # ══════════════════════════════════════════════════════════════════════════════
# # TODO: ما الناتج ؟
result=[x * 2 for x in range(5) if x > 1]
# # OUTPUT: [4,6,8]
# ══════════════════════════════════════════════════════════════════════════════
# TODO: Nested List Comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [n for row in matrix for n in row]
print(result)
# ══════════════════════════════════════════════════════════════════════════════
# TODO: الاعداد التي تقبل القسمه على 3 ولا تقبل القسمه على 2
result =[n for n in range(1,51) if n %3 ==0 and n %2 !=0]
print(result)
# ══════════════════════════════════════════════════════════════════════════════
# TODO: ما الناتج 
[(x, y) for x in [1, 2] for y in [10, 20, 30]]
[(1,10),(1,20),(1,30),(2,10),(2,20),(2,30)]
# ══════════════════════════════════════════════════════════════════════════════
# TODO: تحدي
words = ["python", "java", "ai", "machine", "learning"]
result= [ len(word) for word in words if len(word) >3 ]
print(result)
# ══════════════════════════════════════════════════════════════════════════════
# TODO: concert
result = []
for x in range(1, 6):
    for y in range(1, 6):
        if x * y > 10:
            result.append(x * y)
# ----
result=[ x*y for x in range(1,6) for y in range(1,6) if x*y >10]
print(result)
# ══════════════════════════════════════════════════════════════════════════════
# TODO: correct it if wrong
# [x for x in range(10) if x > 3 else 0]
result=[x if x > 3 else 0 for x in range(10) ]
print(result)
