# ╭─────────────────────────────╮
# │ [ListComps VS Map & Filter] │
# ╰─────────────────────────────╯
# FUNCTION: Map take tow param (1.) function, (2.) itrerable => Applies the function in all elements in iterable and return an iterator as object for this reasone we must use list func to show output  
numbers =[1,2,3,4,5,6,7,8,9]
result =map(lambda x :x**2,numbers)
print(list(result))
# OUTPUT: [1, 4, 9, 16, 25, 36, 49, 64, 81]
# ══════════════════════════════════════════════════════════════════════════════
# FUNCTION: filter take the same param map , but it test a condetion
result =filter(lambda y :y**2 >36, numbers)
print(list(result))
# ══════════════════════════════════════════════════════════════════════════════
# NOTE: sumerrize : map =convert elements, filter = chose elements.
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
