# Choosing random character from given name
import random
name = 'Code Base'
char = random.choice(name)
print("Random character is: ",char)
 # Implementing different things on list
list1 = ["Omar","Imran","Ismail","Shahid","Bilal","Hasnain","Asim"]
list2 = ["Mats","Muzammil","Mahad","Fahad"]
list3 = list1 + list2
print(list3)
list.sort(list1)
print(list1)
list.pop(list2)
print(list2)
list.reverse(list3)
print(list3)
list3.extend(["Fazeel"])
print(list3)
x = list3.index("Fazeel")
print(x)
