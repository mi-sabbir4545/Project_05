class student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA: {self.gpa}")


rahim = student()
# print(isinstance(rahim, student))
rahim.set_value(101, 3.67)
rahim.display()

karim = student()
# print(isinstance(rahim, student))
karim.set_value(102, 4.5)
karim.display()
