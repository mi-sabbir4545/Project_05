
#student1 = ['David', 'mail@gmail.com', '12345678', 'Ny']
#student2 = ['Munsur', 'munsur@gmail.com', '12345678', 'DhAKA']

#print(student1[0])
#print(len(student1))

#student2_name = student2[0]
#print(student2_name)

#guest = ['David', 'munsur', 'lekhon', 'minhaj', 'sujit', 'mahbub', 'asif', 'ruman', 'toukir', 'hridoy']

#lunch = ['David', 'munsur', 'lekhon', 'minhaj', 'sujit']
#dinner = ['mahbub', 'asif', 'ruman', 'toukir', 'hridoy']

#print(guest)

#lunch_guest = [[guest[0], guest[2], guest[3], guest[4], guest[4]]

#lunch_guest = guest[0:5]

#dinner_guest = guest[5:]
#special_guest = guest[2]

#print(lunch_guest)
#print(dinner_guest)

#number = [12,23,3,42,23,3,44]
#number.sort()
#print(number)

#number.insert(3,10)
#print(number)

#number.remove(23)
#print(number)

#number.reverse()
#print(number)

#number.append(100)
#print(number)

#number.clear()
#print(number)


#l = [56,34,67,89,100]
#for index, value in enumerate(l, start= 1):
#    print(index, value)

#l = [56,34,67,89,100]
#for index in range (len(l)):
  #  value = l[index]
   # print(index, value)

#print(l[3])

guest = ['sabbir','ruman','toukir','lekhon','minhaj']

lunch_guest = guest[1:3]
dinner_guest = guest[1:]

print(lunch_guest, dinner_guest)

special_guest = guest[1:2]
print(special_guest)
print(len(guest))

for index, value in enumerate(guest):
    print(index, value)

for index in range (len(guest)):
    value = guest[index]
    print(index,value)

number = [12,3,5,6,7,55,77]
number.sort()
print(number)

number = [12,3,5,6,7,55,77]
number.reverse()
print(number)

number = [12,3,5,6,7,55,77]
number.append(99)
print(number)

number = [12,3,5,6,7,55,77]
number.insert(3,7)
print(number)

pets = ["Dog", "Cat", "Rabbit"]
print(pets[0])
print(pets[2])
print(pets[0:3])
print(pets[-3:-1])
pets.append("Elephent")
print(pets)
pets.insert(0, "Elephent")
print(pets)
pets.pop(1)
print(pets)
pets.remove("Cat")
print(pets)
print(len(pets))
pets[1] = "fish"
print(pets)
pets[0] = "egg"
print(pets)

num1 = [1,2,3]
num2 = [4,5,6]
num1.extend(num2) # extending a list
print(num1)

country = ["India", "Bangladesh", "Australia", "england"]  # check if an exists
check_item = "Australia" in country
print(check_item)
check_item = "pakistan" not in country
print(check_item)






