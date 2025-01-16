class Node:
    def __init__(self, value):
       self.value = value
       self.next = None

class LinkedList:
     def __init__(self):
         self.head = None

     def __repr__(self):
         pass
     
     def __contains__(self):
         pass
     
     def __length__(self):
         pass
     
     def append(self, value):
         if self.head is None:
             self.head = Node(value)
         else:
             last = self.head
             while(last.next is not None):
                 last = last.next
             last.next = Node(value)
     
     def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node
     
     def insert(self, value, index):
         if index is 0:
             self.prepend(value)
         else:
             curr_node = self.head
             count = 0
             while (curr_node.next is not None and count == index):
                 curr_node = curr_node.next
                 count = count+1
     
     def delete(self, value):
         pass
     
     def pop(self, index):
         pass
     
     def get(self, index):
         pass
     
     def print(self):
         pass
     
if __name__ == "__main__":
    pass
