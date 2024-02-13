class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

ll = SingleLinkedList()
ll.insertAtBeginning(10)
ll.insertAtBeginning(20)
ll.insertAtBeginning(30)
ll.print_list()
print("Inserting at the end")
li=SingleLinkedList()
li.insertAtEnd(40)
li.insertAtEnd(50)
li.insertAtEnd(60)
li.print_list()