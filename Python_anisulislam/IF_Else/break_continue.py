"""i = 1
while i <= 100:
    if i == 20:
        break
    print(i)
    i = i + 1

print("Break working")"""

'''i = 1
while i <= 100:
    print(i)
    i = i + 1
    if i == 20:
        break

print("Break working")'''

i = 1
while i <= 100:
    if i == 20:
        continue
    print(i)
    i = i + 1


print('continue working')
