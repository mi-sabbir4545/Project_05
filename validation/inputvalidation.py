while True:

    print("Enter your Age: ")
    age = input()

    try:
        age = int(age)

    except:
        print("Please enter your Age  numeric: ")
        continue


    if age < 0:
        print("Enger age positive: ")
        continue

# print("Your age is: " + str(age))
    break

print(f'Your age is {age}')

