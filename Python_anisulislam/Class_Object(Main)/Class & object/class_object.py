class student:
    roll = ""
    gpa = ""


rahim = student()
# print(isinstance(rahim, student))
rahim.roll = 101
rahim.gpa = 3.4
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

karim = student()
# print(isinstance(rahim, student))
karim.roll = 103
karim.gpa = 3.8
print(f"Roll : {karim.roll}, GPA : {karim.gpa}")
