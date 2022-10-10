while True:
    print("Enter Your Age= ")
    age= input()
    if age.isdecimal():
        print("Valid Input")
        break
    print("Invalid.Please enter your age as Number only")