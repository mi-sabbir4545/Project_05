'''try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)

except ValueError:
    print("You have to insert only integer: ")
except ZeroDivisionError:
    print("You can not divide by zero: ")

finally:
    print("thanks")'''

'''try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)

except (ValueError, ZeroDivisionError):
    print("You have to entered incorrect value: ")

finally:
    print("thanks")'''


def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"


try:
    print(voter(17))
except ValueError as exc:
    print(exc)
