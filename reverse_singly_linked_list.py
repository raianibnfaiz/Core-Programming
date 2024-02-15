class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class ReverseLinkedList:
    def __init__(self):
        self.head = None
    def reverseList(self):
        prev= None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

llist = ReverseLinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverseList()
print("\nReversed Linked List")
llist.printList()

# 1,5,6,8
            
# self.head => 1
            
# current = 1
# next = current.next = 5
# current.next = prev = None
# prev = current = 1
# current = next = 5
