num1 = {1,2,3,4,5,6,7,8,9,10}
num2 = set([1,2,3,4,5])
num2.add(9)

print(num2)
print(4 in num2)
print(4 not in num2)
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)

