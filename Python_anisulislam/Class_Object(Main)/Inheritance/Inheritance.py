# parent class, super class, Base class
# Child class, sub class, Derived class
# Inheritance = to use existing code in subclass
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Samsung(Phone):
    # def call(self):
    #     print("You can call")
    #
    # def message(self):
    #     print("You can message")

    def photo(self):
        print("You can photo")


# p = Phone()
# p.call()
# p.message()

s = Samsung()
s.call()
s.message()
s.photo()
print(issubclass(Samsung, Phone))
print(issubclass(Phone, Samsung))