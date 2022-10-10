birthdays = {'Alice': 'Apr 1', 'Bob': 'May 1', 'Batman': 'mar 1'}

# d = (input("Enter key and value: ").split() for _ in range(birthdays))

while True:
    print("Enter your name")
    name = input()
    if name == '':

        print("Please enter your name")
    else:

    if name in birthdays:
        print(birthdays[name] + " Is your Birthday. ")
        break

    else:
        print("You dont have birthday")
