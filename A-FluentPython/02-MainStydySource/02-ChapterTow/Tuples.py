# ╭──────────╮
# │ [Tuples] │
# ╰──────────╯
# Topic: tuples VS list 
# the important info we need = Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing. Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list
# to learn more => 
# (file:///C:\Users\moham\Documents\dev\Python\B-MasteringPythonWithElzero\007-Modules\namedtuple.py)
# Topic: Tuples as Records
lax_coordinates = (33.9425, -118.408056) # (1)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014) # (2)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')] #(3)
for passport in sorted(traveler_ids): #(4) sorted() function will sort the list of tuples based on the first element of each tuple (the country code) in ascending order. The sorted list will be:
# [('BRA', 'CE342567'), ('ESP', 'XDA205856'), ('USA', '31195855')]
    print('%s/%s' % passport) #(5)
    # NOTE: %s/%s معامل تنسيق نصوص % يفهم الـ tuples ويعامل كل عنصر فيها كحقل منفصل
for country, _ in traveler_ids: #(6) 
#_ is a  IMPORTANT:  dummy variable that we use to ignore the second element of the tuple (the passport number) since we are only interested in the country code. This is a common convention in Python when you want to unpack a tuple but don't need all of its elements.
    print(country)
# OUTPUT: BRA/CE342567 ESP/XDA205856 USA/31195855 USA BRA ESP
#===============================================================#
# Eplain
# (1):Latitude and longitude of the Los Angeles International Airport.
# (1.ar):خطوط الطول والعرض لمطار لوس أنجلوس الدولي
# (2):Data about Tokyo: name, year, population (thousands), population change (%), and area (km²).
# (2.ar):بيانات عن طوكيو: الاسم، السنة، عدد السكان (بالآلاف)، التغير السكاني (%)، والمساحة (كيلومتر مربع)
# (3):A list of tuples, each containing a country code and a passport number.
# (3.ar):قائمة من tuples، كل منها يحتوي على رمز الدولة ورقم جواز السفر.
# (4):Iterating over the sorted list of traveler IDs.
# (4.ar):التكرار على قائمة معرفات المسافرين المرتبة.
# (5):Printing each passport in the format "country/passport_number".
# (5.ar):طباعة كل جواز سفر بالتنسيق "الدولة/رقم جواز السفر".
# (6):Unpacking each tuple into country and passport number, but ignoring the passport number
# (6.ar):فك كل tuple إلى الدولة ورقم جواز السفر، مع تجاهل رقم جواز السفر.
# ══════════════════════════════════════════════════════════════════════════════
# ====> file:///C:\Users\moham\Documents\dev\Python\A-FluentPython\02-MainStydySource\02-ChapterTow\Tuples.md