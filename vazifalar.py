import os
os.system("cls")

# students = {
#     "Samandar": 18,
# 	"Muzaffar": 19,
# 	"Xojiakbar": 16,
# 	"Islom": 20,
# 	"Asomiddin": 14,
# 	"Sobitjon": 17,
# 	"Shoxruh": 20
# }
# for name, age in students.items(): 
#     if age >= 18:                 
#         print(name, end=", ") 



login = {
    "jeymsBond" : "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04"
}

username = input("Username kiriting: ")
password = input("Parol kiriting: ")

if username in login:                
    if login[username] == password:  
        print("Hisobga kirdingiz")
    else:                          
        print("Parol notogri")
else:                                
    print("Bunday foydalanuvchi mavjud emas")
