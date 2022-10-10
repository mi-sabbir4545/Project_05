'''def student(id, name, email, password):
    print("ID:", id,"\nName:",name, "\nEmail:", email,"\nPassword:", password)


student(101, "sabbir", "sabbir @ gmail.com", "password")'''

'''def student(*details):
    # print("Name:",details, "ID:",details)
    print(details[0])

student(101, "sabbir",3.75)'''

'''def add(num1, num2):
    sum = num1 + num2
    print(sum)


add(10, 20)'''

'''def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)'''


def student(**details):
    print(details["name"])


student(id=101, name="Anis")

'''add(10, 20, 70)
add(10, 20, 70, 100)
add(10, 20, 70, 100, 300)'''
