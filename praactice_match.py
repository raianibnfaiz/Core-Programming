class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
class Node:
    def __init__(self):
        self.head = None
    def insertAtBeginning(self,data):
        new_node = LinkedList(data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
ll = Node()
ll.insertAtBeginning(10)
ll.insertAtBeginning(20)
ll.insertAtBeginning(30)
ll.insertAtBeginning(40)
ll.print_list()