# -*- coding: utf-8 -*-
"""
دليل المذاكرة التطبيقي للمحاضرة الأولى باستخدام بايثون (Python)
مبني بالكامل على مساق "أساسيات المنطق والتحقق من صحة البراهين الرياضية"

يغطي هذا الملف جميع المفاهيم التي وردت في المحاضرة:
1. السياسات الأكاديمية (حساب درجات التأخير والعمل الجماعي)
2. القضايا والمسندات (Propositions & Predicates)
3. البحث عن أمثلة مضادة (Counterexamples)
4. حدسية غولدباخ (Goldbach's Conjecture)
5. الروابط المنطقية وجداول الحقيقة (AND, OR, NOT, Implication)
6. المجموعات والصفوف المرتبة (Sets vs Tuples) والعمليات عليها
"""

import math

# ==========================================
# 1. سياسة التأخير الأكاديمية (Course Late Policy)
# ==========================================
# تنص السياسة على أن التأخير في أول 50 ساعة يخصم 1% عن كل ساعة تأخير.
# بعد الـ 50 ساعة، تثبت الدرجة عند 50% كحد أدنى حتى نهاية الترم.

def calculate_grade(hours_late):
    """
    حساب النسبة المئوية التي يحصل عليها الطالب بناءً على ساعات التأخير.
    """
    if hours_late <= 0:
        return 100.0  # تسليم في الموعد
    elif hours_late <= 50:
        return 100.0 - hours_late  # خصم 1% لكل ساعة تأخير
    else:
        return 50.0  # تثبيت الدرجة عند 50% كحد أدنى

# تجربة دالة حساب التأخير
print("--- 1. تجربة سياسة التأخير ---")
print(f"تسليم في الموعد: {calculate_grade(0)}%")
print(f"تسليم بعد ساعة واحدة: {calculate_grade(1)}%")
print(f"تسليم بعد 20 ساعة: {calculate_grade(20)}%")
print(f"تسليم بعد أسبوعين (336 ساعة): {calculate_grade(336)}%\n")


# ==========================================
# 2. القضايا والمسندات (Propositions & Predicates)
# ==========================================
# القضية (Proposition) هي جملة تحتمل الصدق أو الكذب (True/False).
# المسند (Predicate) هو جملة تعتمد قيمتها على متغير (Parameter)، وتتحول لقضية عند تعويض المتغير.

# دالة مساعدة للتحقق من الأعداد الأولية
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def CheackPrime(n):
    if n<2 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False  # إذا قبل القسمة، فهو ليس أوليًا
            
    return True
    
# إذا لم يقبل القسمة على أي رقم، فهو أولي 
# أ) المسند (Predicate) يتم تمثيله في البرمجة كـ دالة (Function) تستقبل متغيراً:
def predicate_is_prime(p):
    """مسند يعتمد على المتغير p"""
    return is_prime(p)

# ب) القضية (Proposition) هي القيمة الناتجة (Boolean Value) بعد التعويض أو الجمل الثابتة:
proposition_1 = predicate_is_prime(7)   # True (قضية صائبة)
proposition_2 = predicate_is_prime(12)  # False (قضية خاطئة)

print("--- 2. القضايا والمسندات ---")
print(f"هل الرقم 7 أولي؟ (قضية): {proposition_1}")
print(f"هل الرقم 12 أولي؟ (قضية): {proposition_2}\n")


# ==========================================
# 3. البحث عن مثال مضاد (Counterexample)
# ==========================================
# القضية: "لكل n في الأعداد الطبيعية، فإن n^2 + n + 41 هو عدد أولي"
# الأعداد الطبيعية تبدأ من 0 في هذا المساق.

def check_euler_formula(limit):
    """
    البحث عن أول عدد طبيعي n يكسر القاعدة (مثال مضاد).
    """
    print("--- 3. البحث عن مثال مضاد لمعادلة أويلر ---")
    for n in range(limit):
        val = n**2 + n + 41
        prime_status = is_prime(val)
        if n <= 5 or n >= 39: # طباعة عينات للتوضيح
            print(f"n = {n:2d} -> {n}^2 + {n} + 41 = {val:4d} | هل هو أولي؟ {prime_status}")
        if n == 6:
            print("... (نقاط اختبار متتالية صائبة) ...")
            
        if not prime_status:
            print(f"\n[!] تم إيجاد المثال المضاد! عند n = {n}، الناتج هو {val} وهو عدد غير أولي ({val} = ({n}+1)^2 = {n+1} * {n+1}).")
            return n, val
    return None

check_euler_formula(45)
print()


# ==========================================
# 4. حدسية غولدباخ (Goldbach's Conjecture)
# ==========================================
# تنص على أن: كل عدد زوجي أكبر من 2 هو مجموع عددين أوليين.

def test_goldbach_conjecture(even_num):
    """
    دالة تختبر حدسية غولدباخ لعدد زوجي معين وتجد العددين الأوليين.
    """
    if even_num <= 2 or even_num % 2 != 0:
        return "يجب إدخال عدد زوجي أكبر من 2."
    
    for p1 in range(2, even_num):
        if is_prime(p1):
            p2 = even_num - p1
            if is_prime(p2):
                return p1, p2
    return None

print("--- 4. حدسية غولدباخ ---")
for num in [12, 20, 100]:
    p1, p2 = test_goldbach_conjecture(num)
    print(f"العدد الزوجي {num} = {p1} + {p2} (كلاهما أولي)")
print()


# ==========================================
# 5. الروابط المنطقية والاستلزام (Logical Operators & Implication)
# ==========================================
# الاستلزام (A implies B) يكتب في بايثون رياضياً على شكل: (not A or B)

def implies(A, B):
    """بوابة الاستلزام المنطقي (A => B)"""
    return (not A) or B

# توليد جدول الحقيقة للاستلزام
print("--- 5. جدول الحقيقة للاستلزام (A => B) ---")
print(" A     | B     | A => B ")
print("-----------------------")
for A in [True, False]:
    for B in [True, False]:
        print(f" {str(A):5s} | {str(B):5s} | {str(implies(A, B)):5s}")
print()

# أ) مثال التكافؤ المنطقي للمعاكس الإيجابي (Contrapositive):
# (A => B) يكافئ تماماً (not B => not A)
def check_contrapositive_equivalence():
    equivalent = True
    for A in [True, False]:
        for B in [True, False]:
            original = implies(A, B)
            contrapositive = implies(not B, not A)
            if original != contrapositive:
                equivalent = False
    return equivalent

print(f"هل (A => B) تكافئ المعاكس الإيجابي (not B => not A) منطقياً؟ {check_contrapositive_equivalence()}\n")


# ==========================================
# 6. المجموعات والصفوف المرتبة (Sets vs Tuples)
# ==========================================
# المجموعات (Sets): لا تهتم بالترتيب وتمنع التكرار.
# الصفوف المرتبة (Tuples): تهتم بالترتيب وتسمح بالتكرار.

print("--- 6. مقارنة المجموعات والصفوف المرتبة ---")
# أ) المجموعات في بايثون:
set_a = {6, 1, 2, 0}
set_b = {2, 1, 6, 0}
set_c = {6, 1, 2, 0, 0} # تكرار الصفر

print(f"المجموعة A: {set_a}")
print(f"المجموعة B: {set_b}")
print(f"المجموعة C (مع التكرار في الكود): {set_c}")
print(f"هل المجموعة A تساوي B؟ {set_a == set_b}")
print(f"هل المجموعة A تساوي C؟ {set_a == set_c}")

# ب) الصفوف المرتبة (Tuples) in Python:
tuple_a = (6, 1, 2, 0)
tuple_b = (2, 1, 6, 0)
tuple_c = (6, 1, 2, 0, 0)

print(f"\nالصف المرتب A: {tuple_a}")
print(f"الصف المرتب B: {tuple_b}")
print(f"هل الصف A يساوي B؟ {tuple_a == tuple_b} (لأن الترتيب مختلف)")
print(f"هل الصف A يساوي C؟ {tuple_a == tuple_c} (لأن الطول والتكرار مختلف)")

# ج) العمليات على المجموعات (Union, Intersection, Difference):
print("\nعمليات المجموعات:")
A = {6, 1, 2, 0}
B = {2, 3, 4} # لنفترض أن B هنا تحتوي العناصر 2، 3، 4 مباشرة لتسهيل التطبيق الحسابي

print(f"المجموعة A = {A}")
print(f"المجموعة B = {B}")
print(f"الاتحاد (A Union B): {A.union(B)}")
print(f"التقاطع (A Intersect B): {A.intersection(B)}")
print(f"الفرق (A - B): {A.difference(B)}")

# د) بناء المجموعات بالشرط المنطقي (Set Builder Notation via List Comprehensions):
# في المحاضرة: { n in N | n is prime }
primes_under_30 = {n for n in range(30) if is_prime(n)}
print(f"\nبناء المجموعة بالشرط المنطقي (الأعداد الأولية تحت 30): {primes_under_30}")
