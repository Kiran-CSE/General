# Using Polymorphic built-in functions
# print(len("Anaconda"))  # 8 Characters
# print(len([5, 15, 20, 25])) # 4 elements

#  Using Polymorphic User-defined functions
# def add(x, y, z = 0):
#     return x + y + z

# print(add(5, 7)) # 12
# print(add(5, 7, 9)) # 21

# Method Overriding
class Bird:
    def intro(self):
        print("Hi, there are many types of birds!")
    
    def flight(self):
        print("Most of birds can fly but some cannot!")
# Sparrow child class
class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly!")
# Ostrich child class
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly!")

# Objects
bird01 = Bird()
sparrow01 = Sparrow()
ostrich01 = Ostrich()

# Call intro and flight
bird01.intro()
bird01.flight()

sparrow01.intro()
sparrow01.flight()

ostrich01.intro()
ostrich01.flight()


