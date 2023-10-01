# Person Parent class
class Person:
    def person_data(self, name, age):
        print("Hello from the Person class!")
        print("the name is:", name,"and the age is:", age)

# Company Parent class
class Company:
    def company_data(self, comp_name, location):
        print("Welcome to the company!")
        print("The company name is:", comp_name, "and location is:", location)

# Employee child class
class Employee(Person, Company):
    def employee_data(self, salary, skill):
        print("Welcome to the Employee class")
        print("Salary is:", salary, "Skill is:", skill)

# Objects for employee
emp01 = Employee()

# Get data on screen
emp01.person_data("Ronaldo", 35)
emp01.company_data("ABCD", "location001")
emp01.employee_data(10000, "Data Science")