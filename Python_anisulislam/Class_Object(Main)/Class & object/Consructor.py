class student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA: {self.gpa}")


rahim = student(101, 3.75)
# print(isinstance(rahim, student))
# rahim.set_value(101, 3.67)
rahim.display()

karim = student(102, 4.5)
# print(isinstance(rahim, student))
# karim.set_value()
karim.display()
