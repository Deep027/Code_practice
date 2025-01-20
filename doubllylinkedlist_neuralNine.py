class Node:
    def __init__(self, value):
       self.value = value
       self.next = None
       self.previous = None

class DoublyLinkedList:
     def __init__(self):
         self.head = None
         self.tail = None

     def __repr__(self):
         if self.head is None:
             return "[]"
         else:
             last = self.head
             return_string = f"[{last.value}"
             while last.next is not None:
                 last = last.next
                 return_string += f", {last.value}"
             return_string += "]"
             
             return return_string
     
     def __contains__(self, value):
         last = self.head
         while(last.next is not None):
             if last.value == value:
                 return True
             last = last.next
         return False
     
     def __length__(self):
         last = self.head
         counter = 0
         while(last is not None):
             counter += 1
             last = last.next
         return counter
     
     def append(self, value):
         if self.head is None:
             self.head = Node(value)
             self.tail = self.head
         else:
             last_node = Node(value)
             last_node.previous = self.tail
             self.tail.next = last_node
             self.tail = last_node

     def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node
     
     def insert(self, value, index):
         if index == 0:
             self.prepend(value)
         else:
             if self.head is None:
                 raise ValueError("Index out of bounds")
             else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node
                
     
     def delete(self, value):
         last = self.head
         flag = 0
         if last is None:
             raise ValueError("The linked list is empty")
         else:
             if (last.value == value):
                 self.head = last.next
                 flag = 1
             else:
                 while last.next is not None:
                     if (last.next.value == value):
                         if (last.next.next is not None):
                             last.next.next.previous = last
                         last.next = last.next.next
                         flag = 1
                         break
                     last = last.next
         if (flag == 0):
             raise ValueError("Value doesn't exists in the list")
                     
     
     def pop(self, index):
         if self.head is None:
             raise ValueError("Index out of bounds")
         else:      
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                    raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next
             
     def get(self, index):
         if self.head is None:
             raise ValueError("Index out of bound")
         last = self.head
         for i in range(index):
             if last.next is None:
                 raise ValueError("Index out of bound")
             last = last.next
         return last.value
     
if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.append(10)
    ll.insert(5,1)
    ll.insert(20,1)
    ll.insert(18,1)
    ll.insert(22,1)
    ll.insert(88,1)
    ll.insert(97,1)
 
    ll.prepend(100)

    ll.insert(200, 1)

    ll.delete(18)
    ll.delete(22)
    ll.delete(5)    

    ll.pop(1)

    print(ll.get(1))
    print(29 in ll)
    print(800 in ll)

    print(ll)


