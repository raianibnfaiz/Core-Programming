class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtbeginning(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

ll = LinkedList()
ll.insertAtbeginning(5)
ll.insertAtbeginning(8)
ll.insertAtbeginning(9)
ll.printList()
ll.reverseList()
print("\nReversed Linked List")
ll.printList()
