from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print("Inserted value: ", x)
    @abstractmethod
    def task(self):
        print("Hi, we are inside Absclass task")

# test child class
class test_class(Absclass):
    def task(self):
        print("Hi, we are inside test_class task")

# example child class
class example_class(Absclass):
    def task(self):
        print("Hi, we are inside example_class task")

# Objects of test_class
test01 = test_class()
test01.task()
test01.print(50)

# Objest of example_class
example01 = example_class()
example01.task()
example01.print(150)

# Testing
print("test01 is instance of Absclass? ", isinstance(test01, Absclass))
print("example01 is instance of Absclass? ", isinstance(example01, Absclass))
