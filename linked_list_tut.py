class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            self.next = self.head
            self.head = new_node
    
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        while (current_node != None and (position + 1) != index):
            position = position + 1
            current_node = current_node.next 

        if (current_node != None):
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Invalid Index")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node

    def updateNode(self, val, index):
        position = 0
        current_node = self.head
        if (index == position):
            self.data = val
        else:
            while(current_node != None and position != index):
                current_node = current_node.next
                position = position + 1
            if (current_node != None):
                current_node.data = val
            else:
                print("Index not present")
    
    def remove_first_node(self):
        if (self.head is None):
            return
        self.head = self.head.next

    def remove_last_node(self):
        if (self.head is None):
            return
        
        current_node = self.head
        while(current_node != None and current_node.next != None):
            current_node = current_node.next
        
        current_node.next = None

    def remove_at_index(self, index):
        if (self.head is None):
            return

        position = 0
        current_node = self.head
        if (index == 0):
            self.remove_first_node()
        
        while (current_node != None and position < index - 1):
            current_node = current_node.next
            position = position + 1
        
        if (current_node is None and current_node.next is None):
            print("Index does not exist")
        else:
            current_node.next = current_node.next.next

    def remove_node(self, data):
        current_node = self.head

        # Check if the head node contains the specified data
        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
    
    def addTwoNumbers(self, l1):
        print(l1.data)
        print(l1.next)


obj = LinkedList()
print("adding first element")
obj.insertAtBegin(23)
obj.printLL()
print(obj.sizeOfLL())
print("adding second element")
obj.insertAtBegin(33)
obj.printLL()
print(obj.sizeOfLL())

# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)
llist.insertAtEnd('e')
llist.insertAtEnd('f')

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.remove_first_node()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last_node()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

# print("\nUpdate node Value at Index 0:")
# llist.updateNode('z', 0)
# llist.printLL()

print("\nSize of linked list:", llist.sizeOfLL())

llist.addTwoNumbers(llist)