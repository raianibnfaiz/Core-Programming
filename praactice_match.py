class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtbeginning(self,data):
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.data , end= " ")
            temp = temp.next

ll = LinkedList()
ll.insertAtbeginning(9)
ll.insertAtbeginning(8)
ll.insertAtbeginning(5)
ll.insertAtbeginning(3)
ll.printList()
print("\n insert at the end now")
ll.insertAtEnd(4)
ll.printList()

      








#3->5->8->9
        
        #3->5->8->9->4

        #3 = self.head
        