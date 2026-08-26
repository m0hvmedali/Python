# membership control
# عندنا قايمه بها مشرفين هم فقط المسموح لهم بالدخول وعندنا صفحه تسجيل دخول بها اسم المستخدم واذا كان اسم المستخدم موجود في القائمه يسمح له بالدخول واذا لم يكن موجود يمنعه من الدخول ويسمح لاي مشرف بحذف او اضافه او تعديل لاي مشرف اخر

# ====================== json =============================#
import json

def save_admins(admins):
    with open("admins.json", "w") as file:
        json.dump(admins, file)

# ======================== start ===========================#

name = input("Enter Your Name: ").capitalize().strip()
with open("admins.json", "r") as f:
    admins = json.load(f)
# ======================== login ===========================#
if name in admins:
    print(f"Hello {name} You Are Admin")
    action = input("Do You Want To Add Or Delete Or Update Admin: ").capitalize().strip()
    # ======================= add ===========================
    if action == "Add":
        new_admin = input("Enter New Admin Name: ").capitalize().strip()
        if new_admin in admins:
            print(f"Admin {new_admin} Already Exists")
        else:
            admins.append(new_admin)
            save_admins(admins)
            print(f"Admin {new_admin} Added Successfully")
        #======================= delete ===========================
    elif action == "Delete":
        admin_to_delete = input("Enter Admin Name To Delete: ").capitalize().strip()
        if admin_to_delete in admins:
            admins.remove(admin_to_delete)
            save_admins(admins)
            print(f"Admin {admin_to_delete} Deleted Successfully")
        else:
            print(f"Admin {admin_to_delete} Not Found")
            # ======================== update ===========================
    elif action == "Update":
        old_admin = input("Enter Admin Name To Update: ").capitalize().strip()
        if old_admin in admins:
            new_admin = input("Enter New Admin Name: ").capitalize().strip()
            if new_admin in admins:
                print(f"Admin {new_admin} Already Exists")
            else:
                admins[admins.index(old_admin)] = new_admin
                save_admins(admins)
                print(f"Admin {old_admin} Updated Successfully")
        else:
            print(f"Admin {old_admin} Not Found")
    else:
        print("Invalid Action")
# ===================== end =============================#

print(f"Current Admins: {admins}")
# ------------------------------------------------------------#
