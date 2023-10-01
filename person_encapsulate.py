class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private member

    # getting age
    def get_age(self):
        return self.__age

    # Setting age
    def set_age(self, age):
        self.__age = age

person01 = Person("Ronaldo", 35)   

# Getting private age for person01
print("Name:", person01.name,"age", person01.get_age())

# Modify age
person01.set_age(36)

print("Name:", person01.name,"age", person01.get_age())