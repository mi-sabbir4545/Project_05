try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")

except ZeroDivisionError:
    print("Division failed")

# '''except IndexError:
#     print("Index failed")'''

finally:
    print("Succesful")
