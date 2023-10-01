class Employee:
    # class constructor
    def __init__(self, name, salary, project):
        self.__name = name
        self._salary = salary
        self.project = project

    # show the employee data
    def show_details(self):
        print("The name is:", self.__name, "and Salary is:", self._salary)

    # Working project
    def work(self):
        print(self.__name, "is working on", self.project)
    
 # Objects for employee
employee01 = Employee("Marcelo", 9000, "Video Game")

# Access public name
# print("The value of name is:", employee01.__name)
# # call the public methods for details
employee01.show_details()
employee01.work()



