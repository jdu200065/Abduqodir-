import os
os.system("cls")

car1 = {
    "brand": "GM",
    "model": "Malibu", 
    "rang": "Qora", 
    "yil": "2025", 
    "proberg": 10_000, 

}
# car1['narxi'] = 20_000

# print(car1)
# car1["model"] = 'Malibu' 
# print(car1["model"])

# if "brand" in car1:
#     print('Yes')
# else:
#     print("No")

# for n in car1:
#     if car1[n] == 'Malibu':
#         print("Bor")
#         break
#     # print(n, car1[n])
# else:
#     print("Yo'q")

# print(car1['Brand'])
# print(car1.get("Brand", 'Bunday brand yoq'))

# print(car1.keys())

# print(car1.values())

# print(car1.pop('yil'))
# print(car1)

# print(car1.items())
# for k, v in car1.items():
#     print(k, v)

# car2 = car1
# print(car2)
# car2 = car1.copy()

# car1.popitem()
# car1.popitem()
# print(car1)


car1['Narx'] = 20_000
car1["model"] = 'Cobalt'
car1['rang'] = 'oq'

new_data = {'Narx': 20_000, 'model':'Cobalt', 'rang':'oq'}
car1.update(new_data)

print(car1)