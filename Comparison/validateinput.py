while True:
    print("Enter Your Age= ")
    age= input()
    if age.isdecimal():
        break
    print("Invalid.Please enter your age as Number only")

while True:
        print('Select a new password (letters and number only): ')
        password = input()
        if password.isdecimal():
            break
        print("Password can only have letters and numbers: ")

