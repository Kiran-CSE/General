# class Snake:
#     """Snake main blueprint"""
#     name = "Anaconda"

#     # Method to change name
#     def modifyName(self, new_name):
#         self.name = new_name

# # Objects based on Snake
# snake01 = Snake()

# # printing on screen
# print(snake01.name)

# # Modify the name using modifyName
# snake01.modifyName("Python")
# print(snake01.name)


# Using Dunder init and instance attributes
class Snake:
    """Snake main blueprint"""
    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName

# Objects
anaconda01 = Snake("Anaconda")
python01 = Snake("Python")

# printing the value of name for the two objects
print(anaconda01.name)
print(python01.name)