import json

# # ========================import data from admins.json=========
def load_admins(admins):                                      #
    with open("admins.json", "r") as file:                    #
                                                              #
        admins = json.load(file)                              #
    return admins                                             #
                                                              #
# # ==============================================================================
# 01
data = load_admins([])

# print (data) # data is a list in json file 
l =int (len(data)) #len =10
# print (l)

a= int(input("input tha started number: "))

while a < l :
    print(f"#{str(a+1).zfill(2)}: {data[a]}")
    a+=1

# # we not wanted this now :
# # # else:
# # print("not valid index")
# 02
# # ================================================================================
# # دلوقتي هنعمل تطبيق بوك مارك ظريف يكون معانا قايمه بها عدد محدد من كتب المفضله لدى المستخدم ونسمح للمستخدم بالتعديل واضافه 
# # اول حاجه القايمه نفسها

fav_book =[] 
max_fav=5

if len(fav_book) == 5 :
    print ("your list is full, sorry")

else :

    while max_fav > 0 :
        add_fav_book = input("write fav here: ").strip()
        fav_book.append(add_fav_book)
        max_fav-=1
        print(f"you have {max_fav} left")
        print(fav_book)

# 03
# ====================================================== for loop practice 
# it's a test of 
my_range = range(1, 100)

for number in my_range: 
    print(number)

my_skills = {

    'py' : '30',
    'js' : '20',
    'html' : '40',
    'css' : '25',
    'c++' : '100'
}

for skill , level in my_skills.items():
    print(f"{skill} : {level}")
# ========================================================
# 04
# loop for nested loop
people ={"osama","ahmed","mohamed","ali","omar"}
# هنا دي قايمه عاديه جدا للناس
skills = ["python","js","html","css","c++"]
# ودى قايمه عاديه جدا للمهارات

for person in people:
    # اول حاجه نعمل لووب على قايمه الاشخاص ونقوله يلف على ال people ويجيب مل person لوحده
    print(person)
    # تانى حاجه نعمل لووب على قايمه المهارات ونقوله يلف على ال skills ويجيب مل skill لوحده
    for skill in skills:
        print(skill)
    # ودى بقى عشان نطبع مسافه فاضيه بعد كل شخص عشان يبان ان ده شخص ودى مهاراته
    print("-" * 20)

# السؤال اللي يطرح نفسه طيب لو مش كل الاشخاص عندهم كل المهارات من غير ما نكبر الدنيا  يعني ببساطه عندنا قايمه فيها اشهاص وقايمه تانيه فيها مهارات عايزين نحدد مهارات كل شخص خلينا نجرب نحط شرط
for person in people:
    print(person)
    if person == "osama":
        print(f"skills of {person} : {skills[0:3]}")
    elif person == "ahmed":
        print(f"skills of {person} : {skills[1:4]}")
    elif person == "mohamed":
        print(f"skills of {person} : {skills[2:5]}")
    elif person == "ali":
        print(f"skills of {person} : {skills[3:6]}")
    elif person == "omar":
        print(f"skills of {person} : {skills[4:7]}")
    else:
        print(f"skills of {person} : {skills}")
    print("-" * 20)
# او ممكن نعمل حاجه ظريفه اننا نستخدم القاموس

peoples ={

    "ahmed":{
        "skills":{
        "python":"50%"
        ,"js":"30%"
        ,"html":"40%"
        ,"css":"25%"
        ,"c++":"100%"
        },
        "age":20
    },
    "mohamed":{
        "skills":{
        "python":"50%"
        ,"js":"30%"
        ,"html":"40%"
        ,"css":"25%"
        ,"c++":"100%"
        },
        "age":20
    },
    "ali":{
        "skills":{
        "python":"50%"
        ,"js":"30%"
        ,"html":"40%"
        ,"css":"25%"
        ,"c++":"100%"
        },
        "age":20
    },
    "omar":{
        "skills":{
        "python":"50%"
        ,"js":"30%"
        ,"html":"40%"
        ,"css":"25%"
        ,"c++":"100%"
        },
        "age":20
    },
    "osama":{
        "skills":{
        "python":"50%",
        "js": "30%",
        "html": "40%",
        "css": "25%",
        "c++": "100%"
        },
        "age":20
    }
}

for person in peoples:
    print(person)
    for skill in peoples[person]["skills"]:
        print(f"{skill} : {peoples[person]["skills"][skill]}")
    print(f"age of {person} is {peoples[person]["age"]}")
    print("=" * 20)

# =============================================
# 05
# break and continue and pass
# =============================================
# example of break
for i in range(10):
    if i == 5:
        break
    print(i)
# example of continue
for i in range(10):
    if i == 5:
        continue
    print(i)
# example of pass

for i in range(10):
        pass
    # لو مش عايز اعمل حاجه هنا دلوقتي ف سيبها وعدي ولا كانك شايف
    

# Advanced Dictionary

mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

print(mySkills.items())

#######################

for skill in mySkills:

  print(f"{skill} => {mySkills[skill]}")

#######################

for skill_key, skill_progress in mySkills.items():

  print(f"{skill_key} => {skill_progress}")

#######################

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in myUltimateSkills.items():

  print(f"{main_key} Progress Is: ")

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")

