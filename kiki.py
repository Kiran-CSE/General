class Node:
    def __init__(self,value):
       self.value=value
       self.next=None
class LinkedList:
    def __init__(self,value):
        new_node= Node(5)
        self.head=new_node
        self.tail=new_node
        self.length=1

my_linked_list = LinkedList(6)
print(my_linked_list.head.value)
