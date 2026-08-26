# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------
import os

# -----------------------------------------------
# -----------------------------------------------
myFile = open("D:\Python\Files\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"D:\Python\Files\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("D:\Python\Files\osama.txt", "w")
myFile.writelines(myList)

myFile = open("D:\Python\Files\osama.txt", "a")
myFile.write("Elzero")


# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------


myFile = open("D:\Python\Files\osama.txt", "a")
myFile.truncate(5)

myFile = open("D:\Python\Files\osama.txt", "a")
print(myFile.tell())

myFile = open("D:\Python\Files\osama.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("D:\Python\Files\osama.txt")