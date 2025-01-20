# class Node:

#     def __init__(self):
#         self.children = dict()
#         self.is_End_of_Word = False

# class test:

#     def __init__(self):
#         self.root = Node()

#     def ins(self):
#         curr = self.root
#         print(f"before ins = {curr.children}")
#         curr.children['a'] = Node()
#         curr.children['c'] = Node()
#         print(f"after ins = {curr.children}")
#         curr = curr.children['a']        
#         print(f"when current becomes next = {curr.children}")
#         curr.children['b'] = Node()
#         print(f"after ins = {curr.children}")
#         curr = curr.children['b']        
#         print(f"when current becomes next = {curr.children}")

# obj = test()
# print(obj.root)
# obj.ins()
# i = 1
# while (i is not 9):
#     print(i)
#     i = i + 1

for i in range(1):
    print("Deep")