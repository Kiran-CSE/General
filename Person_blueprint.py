class Person:
    """Person main class"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

    def display_data(self):
        print("Hi my name is", self.name,",my age is", self.age, 
        "and my personID is", self.personID)

person01 = Person("Ahmed", 29, 120)
person02 = Person("Ronaldo", 35, 130)
person03 = Person("Marcelo", 33, 125)

person01.display_data()
person02.display_data()
person03.display_data()

# print(person01.name)
# print(person01.age)
# print(person01.personID)

# print(person02.name)
# print(person02.age)
# print(person02.personID)

# print(person03.name)
# print(person03.age)
# print(person03.personID)